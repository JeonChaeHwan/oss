{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNMTYVRwVzMqsHWBqah8pyM",
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
        "<a href=\"https://colab.research.google.com/github/JeonChaeHwan/oss/blob/main/setup.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Mt7MWYbQQcDK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "dfef55f5-56b2-44e9-a66c-be837431423b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing mycalc.calculator.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile mycalc.calculator.py"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "_VpDb1dsQiub"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}