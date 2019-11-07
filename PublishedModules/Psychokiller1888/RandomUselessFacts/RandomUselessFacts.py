import html

import requests
from requests.exceptions import RequestException

from core.base.model.Module import Module
from core.util.Decorators import Decorators, IntentWrapper
from core.dialog.model.DialogSession import DialogSession


class RandomUselessFacts(Module):
	"""
	Author: Psychokiller1888
	Description: Gets you the daily random useless fact or a random one
	"""

	@IntentWrapper('GetUselessFact')
	@Decorators.anyExcept(exceptions=(RequestException, KeyError), text='error', printStack=True)
	@Decorators.online
	def uselessFactIntent(self, session: DialogSession, **_kwargs):
		ttype = session.slotValue('type') or 'random'

		response = requests.get(url=f'https://uselessfacts.jsph.pl/{ttype}.json?language={self.activeLanguage()}')
		response.raise_for_status()
		self.endDialog(sessionId=session.sessionId, text=html.unescape(response.json()['text']))
