## Development
This repository demonstrates AI / Machine Learning workflows using AutoGluon AutoML framework.
本專案為一個 AI / Machine Learning 能力培養與實作平台，透過 AutoML 技術與 AutoGluon 框架，協助使用者快速建立與測試不同類型的 AI 模型。

## 專案特色
- 以 AutoML 技術降低 AI 模型建立門檻
- 提供表格資料、時間序列與多模態學習範例
- 可透過 Jupyter Notebook 進行模型訓練與測試
- 提供 Docker 環境，方便快速部署與操作

## AI 任務類型補充說明
本專案提供多種 AI / Machine Learning 任務範例，包含：
- 表格資料預測（Tabular Prediction）
- 時間序列預測（Time Series Forecasting）
- 多模態學習（Multimodal Learning）
透過不同類型的範例，使用者可以快速理解各種資料型態在 AI 模型中的應用方式。

相關文件：

[machine learning](./docs/machine learning)
[autogluon.timeseries](./docs/autogluon.timeseries)
[autogluon.tabular](./docs/autogluon.tabular)
[autogluon.multimodal](./docs/autogluon.multimodal)

# 使用技術
本專案使用以下 AI / Machine Learning 技術：
- AutoGluon AutoML Framework  
- Python Machine Learning  
- Jupyter Notebook  
- Docker GPU 運行環境  

# 啟動 AI 環境
docker run -it --name autogluon -d  --shm-size=16g  --gpus all \
                            -p 17001:8888 \
                            -v $(pwd)/AG:/home/sagemaker-user/src  \
                            --workdir /home/sagemaker-user/src  \
                            shawoo/sagemaker bash -c "jupyter lab --allow-root --ip=0.0.0.0 --ServerApp.disable_check_xsrf=True --NotebookApp.token=YOURPASSWORD"


