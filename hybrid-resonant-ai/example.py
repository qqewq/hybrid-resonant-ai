import argparse

# Импорт модулей (заглушки)
from src.generator import generate_hypotheses
from src.evaluator import evaluate_resonance
from src.rl_gan import evolve_hypotheses

def main(goal: str):
    print(f"🎯 Цель: {goal}\n")

    # Генерация гипотез
    hypotheses = generate_hypotheses(goal)
    print("📚 Сгенерированные гипотезы:")
    for h in hypotheses:
        print(f"- {h}")

    # Оценка резонансом
    evaluated = evaluate_resonance(hypotheses)
    print("\n📊 Оценка гипотез:")
    for h, score in evaluated:
        print(f"- {h} → score: {score:.3f}")

    # Эволюция с помощью RL + GAN
    refined = evolve_hypotheses(evaluated)
    print("\n🔬 Уточнённые гипотезы:")
    for h in refined:
        print(f"- {h}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hybrid Resonant AI CLI Example")
    parser.add_argument("--goal", type=str, required=True, help="Цель (goal) для алгоритма")
    args = parser.parse_args()
    main(args.goal)
