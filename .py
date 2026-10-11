import java.util.Scanner;

public class Main {

    // Исходная функция f(x) = 2x - 1/tan(x)
    public static double f(double x) {
        return 2 * x - (1.0 / Math.tan(x));
    }

    // Производная функции f'(x) = 2 + 1/(sin(x))^2
    public static double df(double x) {
        double sinX = Math.sin(x);
        return 2.0 + (1.0 / (sinX * sinX));
    }

    /**
     * Реализация метода Ньютона в отдельной функции
     */
    public static double solveByNewton(double x0, double epsilon, int maxIterations) {
        double x = x0;
        
        System.out.println("\n--- Процесс вычислений ---");
        System.out.printf("%-10s | %-12s | %-12s%n", "Итерация", "x", "f(x)");
        System.out.println("---------------------------------------");

        for (int i = 1; i <= maxIterations; i++) {
            double fx = f(x);
            double dfx = df(x);

            // Проверка на нулевую производную во избежание деления на ноль
            if (Math.abs(dfx) < 1e-12) {
                System.out.println("Ошибка: Производная близка к нулю. Метод расходится.");
                return Double.NaN;
            }

            // Формула Ньютона: x_next = x - f(x)/f'(x)
            double xNext = x - fx / dfx;

            System.out.printf("%-10d | %-12.6f | %-12.6f%n", i, xNext, f(xNext));

            // Условие остановки по достижении точности epsilon
            if (Math.abs(xNext - x) < epsilon) {
                System.out.println("---------------------------------------");
                System.out.printf("Успешно! Точность %.5f достигнута на %d-й итерации.%n", epsilon, i);
                return xNext;
            }

            x = xNext;
        }

        System.out.println("---------------------------------------");
        System.out.println("Предупреждение: Достигнуто максимальное количество итераций.");
        return x;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Установка параметров по умолчанию из задания
        double a = 0.0;
        double b = 1.0;
        double epsilon = 0.0001;
        int maxIterations = 100;
        
        // Так как f(0) неопределена (деление на 0), берем x0 ближе к b
        double x0 = b; 

        System.out.println("=== Поиск корня нелинейного уравнения методом Ньютона ===");
        System.out.printf("Уравнение: 2x - 1/tan(x) = 0%n");
        System.out.printf("Отрезок: [%.1f; %.1f]%n", a, b);
        System.out.printf("Точность (ε): %.4f%n", epsilon);
        System.out.printf("Начальное приближение (x0): %.1f%n", x0);

        // Запуск метода Ньютона
        double root = solveByNewton(x0, epsilon, maxIterations);

        // Вывод финального результата
        if (!Double.isNaN(root)) {
            System.out.println("\n=== РЕЗУЛЬТАТ ===");
            System.out.printf("Приближённый корень уравнения: %.6f%n", root);
            System.out.printf("Значение f(корень): %.6e%n", f(root));
        }

        scanner.close();
    }
}
