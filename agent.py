from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

import numpy as np
import random
from collections import deque


class Agent:
	def __init__(self, state_size, is_eval=False, model_name=""):
		self.state_size = state_size
		self.action_size = 3
		self.memory = deque(maxlen=60000)
		self.inventory = []
		self.model_name = model_name
		self.is_eval = is_eval

		self.gamma = 0.5
		self.epsilon = 1.0
		self.epsilon_min = 0.25
		self.epsilon_decay = 0.999981

		self.options = []

		self.model = load_model("models/" + model_name) if is_eval else self.model()

	def model(self):
		model = Sequential()
		model.add(Dense(units=256, input_dim=self.state_size, activation="relu"))
		model.add(Dense(units=256, activation="relu"))
		model.add(Dense(units=256, activation="relu"))
		model.add(Dense(units=256, activation="relu"))
		model.add(Dense(units=256, activation="relu"))
		model.add(Dense(units=256, activation="relu"))

		model.add(Dense(self.action_size, activation="linear"))
		model.compile(loss="mse", optimizer=Adam(lr=0.001))

		return model

	def act(self, state):
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay
			if random.random() <= self.epsilon:
				self.options = None
				return random.randrange(self.action_size)
		self.options = self.model.predict(state)
		return np.argmax(self.options[0])

	def exp_replay(self, batch_size):
		mini_batch = []
		states = []
		target_fs = []

		l = len(self.memory)
		pick = np.random.choice(l, batch_size if batch_size < l else l)
		for i in pick:
			mini_batch.append(self.memory[i])

		for state, action, reward, next_state in mini_batch:
			target = reward + self.gamma * self.model.predict(next_state)[0][action]
			target_f = self.model.predict(state)
			target_f[0][action] = target
			states.append(state[0][:])
			target_fs.append(target_f[0][:])

		self.model.fit([states], [target_fs], epochs=5, verbose=0, batch_size=100)
