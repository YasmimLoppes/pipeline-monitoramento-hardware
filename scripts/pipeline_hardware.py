import pandas as pd
import re
from datetime import datetime

class HardwareDataPipeline:
    def _init_(self):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.raw_data = []
        self.processed_data = None

    def extract_data(self):
        """Simula o Web Scraping de múltiplas fontes (Raw Layer / Bronze)"""
        print(f"[{self.timestamp}] 🔍 Iniciando extração da Camada Bronze...")
        # Simulação de dados brutos vindos de um e-commerce
        self.raw_data = [
            {"id": 101, "item": "GPU NVIDIA RTX 4060 Ti", "price": "R$ 2.549,90", "store": "Kabum"},
            {"id": 102, "item": "GPU NVIDIA RTX 4070 Super", "price": "R$ 4.199,00", "store": "Pichau"},
            {"id": 103, "item": "AMD Radeon RX 7600 XT", "price": "R$ 1.950,00", "store": "Terabyte"},
            {"id": 104, "item": "CPU Intel Core i7-13700K", "price": "R$ 2.899,99", "store": "Kabum"}
        ]
        return self.raw_data

    def transform_data(self):
        """Data Cleaning e Schema Enforcement (Silver Layer / Trusted)"""
        print(f"[{self.timestamp}] ⚙️ Processando dados para a Camada Silver...")
        
        df = pd.DataFrame(self.raw_data)

        # 1. Limpeza de Preço com Regex (Extrai apenas números e converte para float)
        def clean_currency(value):
            clean_val = re.sub(r'[R\$\s\.]', '', value).replace(',', '.')
            return float(clean_val)

        df['price_numeric'] = df['price'].apply(clean_currency)

        # 2. Categorização Automática (Lógica de Engenharia)
        df['category'] = df['item'].apply(lambda x: 'GPU' if 'GPU' in x or 'Radeon' in x else 'CPU')

        # 3. Metadados de Auditoria
        df['extraction_date'] = self.timestamp
        df['status'] = 'Active'

        self.processed_data = df
        return self.processed_data

    def run_pipeline(self):
        """Executa o fluxo completo do Pipeline"""
        self.extract_data()
        final_df = self.transform_data()
        
        print("\n--- 📊 Resultado do Pipeline (Dados Estruturados) ---")
        print(final_df[['item', 'category', 'price_numeric', 'store']])
        
        print(f"\n✅ Sucesso! {len(final_df)} registros prontos para carga no SQL.")

if _name_ == "_main_":
    pipeline = HardwareDataPipeline()
    pipeline.run_pipeline()
