## Development
This repository demonstrates AI / Machine Learning workflows using AutoGluon AutoML framework.
本專案為一個 AI / Machine Learning 能力培養與實作平台，透過 AutoML 技術與 AutoGluon 框架，協助使用者快速建立與測試不同類型的 AI 模型。

## 專案特色
- 以 AutoML 技術降低 AI 模型建立門檻
- 提供表格資料、時間序列與多模態學習範例
- 可透過 Jupyter Notebook 進行模型訓練與測試
- 提供 Docker 環境，方便快速部署與操作



[machine learning](./docs/machine learning)
[autogluon.timeseries](./docs/autogluon.timeseries)
[autogluon.tabular](./docs/autogluon.tabular)
[autogluon.multimodal](./docs/autogluon.multimodal)


docker run -it --name autogluon -d  --shm-size=16g  --gpus all \
                            -p 17001:8888 \
                            -v $(pwd)/AG:/home/sagemaker-user/src  \
                            --workdir /home/sagemaker-user/src  \
                            shawoo/sagemaker bash -c "jupyter lab --allow-root --ip=0.0.0.0 --ServerApp.disable_check_xsrf=True --NotebookApp.token=YOURPASSWORD"


