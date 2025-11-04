import joblib
from xgboost import XGBClassifier
from data_handler import load_model, save_model

class FootballAIPro:
    def __init__(self):
        self.model = load_model()
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
        Treinamento incremental (usando dados recentes)
        """
        self.model.fit(X_new, y_new)
        save_model(self.model)

    def predict(self, X):
        return self.model.predict_proba(X)[:, 1]
