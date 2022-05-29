def oneAway(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    i, j = 0, 0
    edited = False
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif not edited:
            if len(a) > len(b):
                i += 1
            elif len(a) < len(b):
                j += 1
            else:
                i += 1
                j += 1
            edited = True
        else:
            return False
    return True

if __name__ == '__main__':
    print(oneAway('pale', 'ple'))
    print(oneAway('pales', 'pale'))
    print(oneAway('pale', 'bale'))
    print(oneAway('pale', 'bake'))