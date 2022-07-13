#Pegar o Valor Total de um Conta, dividir entre as pessoas e calcular uma porcentagem de gorjeta.
#Mostrat o resultado de quanto cada pessoa deve pagar, incluso a gorjeta.
#Formatar o resultado com 2 casas decimais = ex : 33,60.
print("### Bem-vindo à calculadora de gorjetas! ### \n")
bill = float(input("Qual o valor total da conta? \n R$  "))
tip = int(input("Quanta gorjeta você gostaria de dar? 10%, 12% ou 15%? \n"))
people = int(input("Quantas pessoas para dividir a conta? \n"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)





print(f"Cada pessoa deve pagar: R$ {final_amount}")

#Projeto Desenvolvido por: jB Oliveira para o segundo dia dos #100DaysOfPython