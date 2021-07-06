from django.http import HttpResponse
from django.shortcuts import render
import modern_greek_phonemic_phonetic as g2ipa

def main(request):
    args = {}

    if request.method == 'POST':
        post = request.POST
        input = post.get('input')

        phonemic, phonetic = g2ipa.main(input)

        args['phonemic'] = phonemic
        args['phonemic_split'] = phonemic_split
        args['phonetic'] = phonetic

    return render(request, 'main.html', args)
