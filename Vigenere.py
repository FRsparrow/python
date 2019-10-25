key_len = 6
text = 'JTQHM UPL XCYLCHQNYDg Rlhg EcdngvGpljvmv 1Cv ma u bvceb crqgytaetws igsyiytilryf, bsuv e dcpopm gcv qy rwwapmuqsvzz i ozif jwcnwvi, gwax my qr hupb wq c aqqy.Pseppgz ttnvti vhqer ebg jmpfkvka it zqpqu sn mwkl l oir xua fm ip lqdzkzwb ypbizthi e yykoljzotpswo, blqd vzybs ka az ympt zkfil cp xpp oqrldih xpp ucvzzoplmvr hiqqwcga, ebcb pp ka kzhuqhmcyf xpp tqkpezwt xcirmvbjih wwxy wrm it sbsyt sn njmmz xcckpeyta."Xs liic Oz. Mypvib," aeqo jqw wufg bz jqq zhg hij, "ligy gsc bgivl njixVpnjmvntynl Xllm ma fgb ie niwb?"Oz. Mypvib lgxpqpx blie jm plx vsb."Dcx tn qw," tmxcchgl asy; "nzl Uva. Nwro bca rfmv fmph pizp, irl mjmxwwx ui lfn ejzov mb."Oz. Mypvib gcli yi irahyt."Lz awy yiv aiyn bs vhqe esi pea ncsiv cv?" nlkmh scu aqqy qqxlnkmrbws."_Gzo_ aiyn bs eynt up, irl C pedp pw wmdgkxqzh bs syczmvr kb."Ebka elm qrdtncbmwy gvscrb."Apj, uc oycz, jiw qcdn srwh, Uva. Nwro mcgw ebcb Vpnjmvntynl qd viomyva e jiwvk xup sn fczkm zqzxcyy nvwx vpi yitbl zz Mrowupl; ebcb pp eiqmoiyv wy Owrlls qr l epeqdy irl zqcv ei aim njm xwuem,'
key = [20,2,8,4,8,11]
'''
for i in range(26):
    key[0] = i
    for j in range(26):
        cipher = ''
        key[2] = j
        for i in range(0, 1024):
            if ord('a') <= ord(text[i]) <= ord('z'):
                cipher += chr((ord(text[i]) - ord('a') - key[i % key_len]) % 26 + ord('a'))
            elif ord('A') <= ord(text[i]) <= ord('Z'):
                cipher += chr((ord(text[i]) - ord('A') - key[i % key_len]) % 26 + ord('Z'))
            else:
                cipher += text[i]
        if 'the' in cipher and 'just' in cipher and 'been' in cipher and 'here' in cipher and 'fortune' in cipher :
            print(cipher)
'''
cipher = ''
for i in range(1024):
    if ord('a') <= ord(text[i]) <= ord('z'):
        cipher += chr((ord(text[i]) - ord('a') - key[i % key_len]) % 26 + ord('a'))
    elif ord('A') <= ord(text[i]) <= ord('Z'):
        cipher += chr((ord(text[i]) - ord('A') - key[i % key_len]) % 26 + ord('A'))
    else:
        cipher += text[i]
print(cipher)
