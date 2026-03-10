[machine learning](./docs/machine learning)
[autogluon.timeseries](./docs/autogluon.timeseries)
[autogluon.tabular](./docs/autogluon.tabular)
[autogluon.multimodal](./docs/autogluon.multimodal)


docker run -it --name autogluon -d  --shm-size=16g  --gpus all \
                            -p 17001:8888 \
                            -v $(pwd)/AG:/home/sagemaker-user/src  \
                            --workdir /home/sagemaker-user/src  \
                            shawoo/sagemaker bash -c "jupyter lab --allow-root --ip=0.0.0.0 --ServerApp.disable_check_xsrf=True --NotebookApp.token=YOURPASSWORD"