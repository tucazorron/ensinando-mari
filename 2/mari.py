nota1, nota2, nota3, nota4, nota5 = map(int, input().split())
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(media)
if media >= 7:
    print("Aprovado")
    if media >= 9:
        print("SS")
    else:
        print("MS")
else:
    print("Reprovado")
    print("MM")

# elif media < 4:
#     print("Reprovado")
# mesma coisa do else
# if media < 7:
#     print ("MM")
# elif media < 9:
#     print("MS")
# else:
#     print("SS")

