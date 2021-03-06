{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "FeatureSelection.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMsjawqhqDMPVYRwTvW85mc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kandulanarasimharao/MLPractice/blob/main/FeatureSelection.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "from sklearn import linear_model\n",
        "from sklearn.linear_model import Lasso\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error\n",
        "from sklearn import datasets"
      ],
      "metadata": {
        "id": "juRgzsGXc9uj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_csv(\"./sample_data/diabetes.csv\")\n",
        "data.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "gesVhk7ldn_f",
        "outputId": "ff85e186-2a1d-47b7-8a68-15dffeb922bd"
      },
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
              "0            6      148             72             35        0  33.6   \n",
              "1            1       85             66             29        0  26.6   \n",
              "2            8      183             64              0        0  23.3   \n",
              "3            1       89             66             23       94  28.1   \n",
              "4            0      137             40             35      168  43.1   \n",
              "\n",
              "   DiabetesPedigreeFunction  Age  Outcome  \n",
              "0                     0.627   50        1  \n",
              "1                     0.351   31        0  \n",
              "2                     0.672   32        1  \n",
              "3                     0.167   21        0  \n",
              "4                     2.288   33        1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c635468c-206d-4f42-a1ff-791cf27807cd\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Pregnancies</th>\n",
              "      <th>Glucose</th>\n",
              "      <th>BloodPressure</th>\n",
              "      <th>SkinThickness</th>\n",
              "      <th>Insulin</th>\n",
              "      <th>BMI</th>\n",
              "      <th>DiabetesPedigreeFunction</th>\n",
              "      <th>Age</th>\n",
              "      <th>Outcome</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>6</td>\n",
              "      <td>148</td>\n",
              "      <td>72</td>\n",
              "      <td>35</td>\n",
              "      <td>0</td>\n",
              "      <td>33.6</td>\n",
              "      <td>0.627</td>\n",
              "      <td>50</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>85</td>\n",
              "      <td>66</td>\n",
              "      <td>29</td>\n",
              "      <td>0</td>\n",
              "      <td>26.6</td>\n",
              "      <td>0.351</td>\n",
              "      <td>31</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>8</td>\n",
              "      <td>183</td>\n",
              "      <td>64</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>23.3</td>\n",
              "      <td>0.672</td>\n",
              "      <td>32</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>89</td>\n",
              "      <td>66</td>\n",
              "      <td>23</td>\n",
              "      <td>94</td>\n",
              "      <td>28.1</td>\n",
              "      <td>0.167</td>\n",
              "      <td>21</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>137</td>\n",
              "      <td>40</td>\n",
              "      <td>35</td>\n",
              "      <td>168</td>\n",
              "      <td>43.1</td>\n",
              "      <td>2.288</td>\n",
              "      <td>33</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c635468c-206d-4f42-a1ff-791cf27807cd')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c635468c-206d-4f42-a1ff-791cf27807cd button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c635468c-206d-4f42-a1ff-791cf27807cd');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X=data.drop('Outcome',axis=1).values\n",
        "y=data['Outcome'].values"
      ],
      "metadata": {
        "id": "ZFTDZl7YrMl_"
      },
      "execution_count": 79,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=10)"
      ],
      "metadata": {
        "id": "8t98cUbbtxXZ"
      },
      "execution_count": 83,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X.shape, X_train.shape, X_test.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LU_Z3aNCt_ID",
        "outputId": "61319d13-f0a6-4f71-ea47-63025c3b930f"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "((768, 8), (576, 8), (192, 8))"
            ]
          },
          "metadata": {},
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "reg=Lasso(alpha=0.1)\n",
        "lasso_coef=reg.fit(X_train,y_train).coef_"
      ],
      "metadata": {
        "id": "cmqVILz0GExf"
      },
      "execution_count": 85,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "colnames=list(data.columns)\n",
        "colnames.remove('Outcome')"
      ],
      "metadata": {
        "id": "vW_L5YN4GPV5"
      },
      "execution_count": 87,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.plot(range(len(colnames)),lasso_coef)\n",
        "plt.xticks(range(len(colnames)),colnames,rotation=60)\n",
        "plt.ylabel('COE')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 373
        },
        "id": "9o4-7NGKGUwx",
        "outputId": "906ba6aa-3946-4e62-eb72-f942bbfcb827"
      },
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
