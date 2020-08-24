from fractions import Fraction
import copy
import functools

def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    """"""
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A, B):
    """"""
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    assert colsA == rowsB

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def get_matrixI(t):
    return [[1 if i == j else 0 for i in range(t)] for j in range(t)]

def determinant_fast(A):
    # Section 1: Establish n parameter and copy A
    n = len(A)
    AM = copy_matrix(A)

    # Section 2: Row ops on A to get in upper triangle form
    for fd in range(n): # A) fd stands for focus diagonal
        for i in range(fd+1,n): # B) only use rows below fd row
            if AM[fd][fd] == 0: # C) if diagonal is zero ...
                AM[fd][fd] == 1.0e-18 # change to ~zero
            # D) cr stands for "current row"
            crScaler = AM[i][fd] / AM[fd][fd]
            # E) cr - crScaler * fdRow, one element at a time
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    # Section 3: Once AM is in upper triangle form ...
    product = 1.0
    for i in range(n):
        # ... product of diagonals is determinant
        product *= AM[i][i]

    return product

def get_inverse_matrix(A):

    AM = copy_matrix(A)

    # check if matrix is invertable
    assert determinant_fast(A) != 0.0
    assert len(A) == len(A[0])

    n = len(A)
    I = get_matrixI(n)
    IM = copy_matrix(I)

    indices = list(range(n)) # to allow flexible row referencing ***

    for fd in range(n): # fd stands for focus diagonal

        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.

        for j in range(n): # Use j to indicate column looping.

            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler

        # SECOND: operate on all rows except fd row.
        for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.

            crScaler = AM[i][fd] # cr stands for "current row".

            for j in range(n): # cr - crScaler * fdRow, but one element at a time.

                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    return IM

def get_matrixQ(transitions, t):

    matrixQ = []

    rows = transitions[:t]
    for i in range(len(rows)):
        matrixQ.append(transitions[i][:t])

    return matrixQ

def get_matrixR(transitions, t):

    matrixR = []

    rows = transitions[:t]
    for i in range(len(rows)):
        matrixR.append(transitions[i][t:])

    return matrixR

def get_matrixIminusQ(matrixQ):
    """"""
    matrixIminusQ = copy.deepcopy(matrixQ)

    for i in range(len(matrixQ)):
        for j in range(len(matrixQ[i])):

            prev = matrixIminusQ[i][j]

            if i == j:
                matrixIminusQ[i][j] = 1 - prev
            else:
                matrixIminusQ[i][j] = -prev

    return matrixIminusQ

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

def get_numerators_denominator(matrixB):
    """"""
    probabilities = matrixB[0]
    probabilities = [Fraction(i) if not isinstance(i, Fraction) else i for i in probabilities]
    numerators = [frac.limit_denominator().numerator for frac in probabilities]
    denominators = [frac.limit_denominator().denominator for frac in probabilities]

    LCM = functools.reduce(lambda x, y: lcm(x, y), denominators)

    for i in range(len(numerators)):
        numerators[i] *= int(LCM / denominators[i])

    numerators.append(LCM)

    return numerators

def sortMatrixM(m):
    """"""
    rows = len(m)
    cols = len(m[0])

    transient_states = []
    absorbing_states = []

    for i in range(rows):
        if sum(m[i]):
            transient_states.append(i)
        else:
            absorbing_states.append(i)

    states = transient_states + absorbing_states

    m_ = []
    for i in states:
        m_.append(m[i])

    m_helper = copy.deepcopy(m_)

    for i, st in enumerate(states):

        for row_ in range(len(m_)):

            m_[row_][i] = m_helper[row_][st]

    return m_

def solution(m):
    """"""
    t = 0
    r = 0

    rows = len(m)
    cols = len(m[0])

    assert rows == cols
    assert rows <= 10 and cols <= 10

    if (rows == 1 and cols == 1):
        return [1, 1]


    transitions = []
    absorptions = []

    matrix_sorted = sortMatrixM(m)

    for i in range(rows): # row

        denominator = sum(matrix_sorted[i])

        if denominator:
            t += 1

            trans_ = []

            for j in range(cols): # column

                numerator = matrix_sorted[i][j]
                # append fraction but later check if numerator is 0
                trans_.append(Fraction(numerator, denominator))

            transitions.append(trans_)

        else:
            r += 1
            absorptions.append([0 for ii_ in range(cols)])

    # if there is only 1 transient state, return that one
    if len(transitions) == 1:
        result = get_numerators_denominator(transitions)
        return result

    matrixQ = get_matrixQ(transitions, t)
    matrixR = get_matrixR(transitions, t)

    matrixIminusQ = get_matrixIminusQ(matrixQ)
    matrixN = get_inverse_matrix(matrixIminusQ)
    matrixB = matrix_multiply(matrixN, matrixR)

    result = get_numerators_denominator(matrixB)

    return result


if __name__ == '__main__':

    assert (
        solution([
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]) == [7, 6, 8, 21]
    )

    assert (
        solution([
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]) == [0, 3, 2, 9, 14]
    )
