def FibSeqGen(n : int) -> list:
    fibSeq = [0, 1]

    for i in range(2,n):
        p = fibSeq[i-2]+fibSeq[i-1]
        fibSeq.append(p)
    
    return fibSeq



