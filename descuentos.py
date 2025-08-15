def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >=25:
        if membership == "Gold":
            discount = 0.2
        elif membership == "Silver":
            discount = 0.1      
        elif membership == "Bronze":
            discount = 0.05
        else:
            print(f"Membresia no valida, no te pudimos realizar ningun descuento. Tu total es ${billAmount:,.2f}")          
            return billAmount
        billAmountConDescuento = round(billAmount * (1- discount), 2)
        descuentoAplicado = round(billAmount - billAmountConDescuento, 2)
        print(f"Obtuviste un {discount * 100:.0f}% de descuento con tu membresia {membership}. Ahorraste ${descuentoAplicado:,.2f}.")
        return billAmountConDescuento
    else:
        print("Los descuentos solo se aplican en compras superiores a los $25")
        return billAmount


getDiscount(3423423,"Gold")