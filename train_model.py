from model import train_and_save_model


if __name__ == "__main__":
    metrics = train_and_save_model()
    print(f"Rows used: {metrics['rows']}")
    print(f"R2 score: {metrics['r2']:.4f}")
    print(f"MAE: {metrics['mae']:.4f}")
    print("Model saved successfully.")
