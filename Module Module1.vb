Module Module1
    Sub Main()
        Dim radio As Double
        Dim altura As Double
        Dim area As Double
        Dim volumen As Double
        Dim pi As Double = Math.PI

        Console.Write("Introduce el radio del cilindro: ")
        radio = Convert.ToDouble(Console.ReadLine())

        Console.Write("Introduce la altura del cilindro: ")
        altura = Convert.ToDouble(Console.ReadLine())

    ""Calculamos el área y el  ""
        area = 2 * pi * radio * (radio + altura)
        volumen = pi * Math.Pow(radio, 2) * altura

        Console.WriteLine("El área del cilindro es: " & area)
        Console.WriteLine("El volumen del cilindro es: " & volumen)

        Console.ReadKey()
    End Sub
End Module
