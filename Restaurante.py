def menu():
    print("--𝕽𝖊𝖘𝖙𝖆𝖚𝖗𝖆𝖓𝖙𝖊 𝖉𝖔 𝕱𝖊𝖗𝖓𝖆𝖓𝖉𝖔!--")
    print("1 - Pizza (fatia) -- R$15.00")
    print("2 - Hamburgão ------ R$10.00")
    print("3 - Refrigerante --- R$5.00")
    print("4 - Sobremesa ------ R$10.00")
    print("5 - Finalizar pedido")
    print()
def main():
    pedido = ""
    total_pedido = 0.0
      
    while True:
        menu()
        opcao = input("Escolha o que deseja: ")

        if opcao == '1':
            pedido += "Pizza (fatia) -- R$15,00\n"
            total_pedido += 15.00
        elif opcao == '2':
            pedido += "Hamburgão ------ R$10,00\n"
            total_pedido += 10.00
        elif opcao == '3':
            pedido += "Refrigerante --- R$5,00\n"
            total_pedido += 5.00
        elif opcao == '4':
            pedido += "Sobremesa ------ R$10,00\n"
            total_pedido += 10.00
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

        add_outro = input("Deseja adicionar outro produto? (s/n): ")
        if add_outro.lower() != 's':
            break
    
    print("\nProdutos escolhidos:")
    print(pedido)
    total_pedido_str = "%.2f" % total_pedido
    total_pedido_real = total_pedido_str.replace(".", ",")
    print("Total do pedido: R$%s"%total_pedido_real,"!")

    
if __name__ == "__main__":
    main()