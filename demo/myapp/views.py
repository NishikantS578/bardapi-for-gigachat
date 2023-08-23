from django.http import HttpRequest,HttpResponse,JsonResponse
from bardapi import Bard,BardCookies
import json

def index(request):
	#token='ZggkVGgBAaOOzPhm4rJrrBnKnZ4_vAMPUimDZlV6xs6xqH2vZ5LYp-xw2xDWSNhUQ-i0yA.'
	cookie_dict={
		"__Secure-1PSID":"aAgkVPN5vAwy_rs22eeO4-jH-hUqso4lfAeF_ZDPA1YMmFPup5fexQXVMQztOjmSyciAKA.",
		"__Secure-1PSIDTS":"sidts-CjIBSAxbGQRrb7AGxZZ_SZ1XJIXbje8K6Bmt6oFIVnJkptGUHg1PwUWeypZU9b0A2lBm2hAA",
	}
	data=json.loads(request.body.decode())
	#bard=Bard(token=token)
	bard=BardCookies(cookie_dict=cookie_dict)
	ans=bard.get_answer(data['q'])['content']
	return HttpResponse(ans)
	#return HttpResponse("hello")

# Create your views here.
