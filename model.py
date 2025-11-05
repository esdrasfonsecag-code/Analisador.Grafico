import joblib
from xgboost import XGBClassifier
from data_handler import load_model, save_model

class FootballAIPro:
    def __init__(self):
        # Tenta carregar o modelo salvo
        self.model = load_model()

        # Se não existir modelo salvo, cria um novo
        if self.model is None:
            self.model = XGBClassifier(
                n_estimators=200,
                max_depth=4,
                learning_rate=0.1,
                use_label_encoder=False,
                eval_metric='logloss'
            )

    def update_model(self, X_new, y_new):
        """
        Treinamento incremental com novos dados.
        """
        # Garante que os dados estejam no formato correto
        X_new = X_new if hasattr(X_new, "shape") else [X_new]
        y_new = y_new if hasattr(y_new, "__iter__") else [y_new]

        self.model.fit(X_new, y_new)
        save_model(self.model)

    def predict(self, X):
        """
        Retorna a probabilidade de sair mais de 2.5 gols.
        """
        X = X if hasattr(X, "shape") else [X]
        return self.model.predict_proba(X)[:, 1]
