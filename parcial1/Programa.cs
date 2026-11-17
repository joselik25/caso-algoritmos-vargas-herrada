using System;
using System.Collections.Generic;
using System.Diagnostics;

public static class Caja
{
    public static bool HayComprobantesRepetidosPorPares(int[] comprobantes)
    {
        for (int a = 0; a < comprobantes.Length; a++)
        {
            for (int b = a + 1; b < comprobantes.Length; b++)
            {
                if (comprobantes[a] == comprobantes[b])
                    return true;
            }
        }

        return false;
    }

    public static bool HayComprobantesRepetidosCurado(int[] comprobantes)
    {
        HashSet<int> vistos = new HashSet<int>();

        foreach (int comprobante in comprobantes)
        {
            if (!vistos.Add(comprobante))
                return true;
        }

        return false;
    }

    public static int[] GenerarSinRepetidos(int n, int semilla = 77)
    {
        int[] datos = new int[n];

        for (int i = 0; i < n; i++)
            datos[i] = 1000 + i;

        Random azar = new Random(semilla);

        for (int i = n - 1; i > 0; i--)
        {
            int k = azar.Next(i + 1);
            int temporal = datos[i];
            datos[i] = datos[k];
            datos[k] = temporal;
        }

        return datos;
    }
}

public class Program
{
    private static readonly (int[] datos, bool esperado, string que)[] Casos =
    {
        (new int[] { 1010, 1003, 1009, 1003, 1005 }, true, "repetido en el medio"),
        (new int[] { 1010, 1003, 1009, 1004, 1005 }, false, "sin repetidos"),
        (new int[] { }, false, "lista vacia"),
        (new int[] { 1008 }, false, "un solo elemento"),
        (new int[] { 1004, 1001, 1002, 1006, 1004 }, true, "repetido en los extremos")
    };

    public static void Main()
    {
        Console.WriteLine("PARCIAL 1 - VARIANTE B");
        Console.WriteLine("REGISTRO DE COMPROBANTES");
        Console.WriteLine("-----------------------------------------------");

        bool todosCorrectos = true;

        foreach (var caso in Casos)
        {
            bool lenta = Caja.HayComprobantesRepetidosPorPares(caso.datos);
            bool curada = Caja.HayComprobantesRepetidosCurado(caso.datos);

            Console.WriteLine(
                $"{caso.que,-26} esperado: {caso.esperado,-5} por pares: {lenta,-5} tu cura: {curada,-5}"
            );

            if (curada != caso.esperado)
                todosCorrectos = false;
        }

        Console.WriteLine("-----------------------------------------------");
        Console.WriteLine(todosCorrectos
            ? "RESULTADO: TODOS LOS CASOS SON CORRECTOS."
            : "RESULTADO: HAY CASOS QUE DEBEN CORREGIRSE.");

        int[] grande = Caja.GenerarSinRepetidos(5000);

        Stopwatch reloj = Stopwatch.StartNew();
        Caja.HayComprobantesRepetidosPorPares(grande);
        reloj.Stop();

        Console.WriteLine(
            $"Por pares con 5000 datos: {reloj.ElapsedMilliseconds} ms"
        );

        reloj.Restart();
        Caja.HayComprobantesRepetidosCurado(grande);
        reloj.Stop();

        Console.WriteLine(
            $"Metodo mejorado con 5000 datos: {reloj.ElapsedMilliseconds} ms"
        );
    }
}

