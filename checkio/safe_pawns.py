def safe_pawns(chess):
    return [True if chr(ord(x[0])-1)+str(int(x[1])-1) in chess or chr(ord(x[0])+1)+str(int(x[1])-1) in chess else False for x in chess].count(True)


print(safe_pawns({"a4", "d4", "f4", "c3", "e3", "h5", "d2"})) #== 6

