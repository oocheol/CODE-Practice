 """손실함수는 MSE 외에도 다양하게 존재합니다. 
 지금 보이는 WRMSE는 가중치가 추가된 손실함수 입니다. 
 가중치는 'AB' 라는 변수가 되며, 
 실제 y값은 변수 'OPS', 
 예측된 값은 변수 'Pred' 가 됩니다. 
 위 정보를 참고하여 4명의 야구 선수들의 OPS를 예측한 값의 손실함수 WRMSE 수식을 
 파이썬 코드를 사용하여 작성하되, 
 클래스의 개념이 포함되어야 합니다. 
 그리고 연산의 결과를 제출하시오. """

import numpy as np
import pandas as pd


class WRMSE :
    def __init__(self) :
        self.x = np.array([200, 50, 0, 0])
        self.y = np.array([0.9, 0.4, 0.0, 0.0])
        self.Pred = np.array([0.95, 0.35, 0.5, 0.3])

    def forward_postproc(Pred, y):
        diff   = Pred - y
        square = np.square(diff) 
        sse    = 1/2 * np.sum(square)