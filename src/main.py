from analysis import correlation_matrix, descriptive_analysis
from data_loader import load_data
from preprocessing import preprocess_data
from training import train_and_evaluate_models


def main(data_path: str = "data/iris.csv") -> None:
    data = load_data(data_path)

    desc_stats, class_distribution = descriptive_analysis(data)
    print("Descriptive Statistics:")
    print(desc_stats)
    print("\nClass Distribution:")
    print(class_distribution)

    print("\nCorrelation between Features:")
    print(correlation_matrix(data))

    X, y = preprocess_data(data)
    results = train_and_evaluate_models(X, y)

    for name, result in results.items():
        print(f"\nModel Evaluation {name}:")
        print(f"Accuracy: {result['accuracy']:.4f}")
        print(result["report"])
        print("Confusion Matrix:")
        print(result["confusion_matrix"])


if __name__ == "__main__":
    main()
