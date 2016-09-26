from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import glob
import os


def ls(request):

    # find all subdirs o settings.PIX_HOME_DIR
    home_dir = settings.PIX_HOME_DIR
    sub_dirs = [x[0] for x in os.walk(home_dir)]
    context = {
        'dir': home_dir,
        'sub_dirs': sub_dirs,
    }
    template = loader.get_template('ls.html')
    return HttpResponse(template.render(context, request))


def gallery(request):

    # setup of config variables
    template = loader.get_template('gallery.html')
    relative_dir = request.GET.get('dir')
    regex = relative_dir + '/*'
    promotion_text_addition = settings.PIX_WHEN_PROMOTING_APPEND_THIS_TEXT

    # begin parsing directory
    _dir = settings.BASE_DIR + '/' + regex
    files = glob.glob(_dir)
    if len(files) == 0:
        return HttpResponse(template.render({}, request))
    idx = int(request.GET.get('i',0))
    this_file = files[idx]

    # if there has been a POST request, find and update the filepath.
    try:
        if request.method == 'POST':
            for i in range(0,len(files)):
                last_file = request.POST['file'].replace('.{}'.format(promotion_text_addition),'')
                cur_file = files[i].replace(settings.BASE_DIR,'').replace('.{}'.format(promotion_text_addition),'')
                if cur_file == str(last_file):
                    idx = i
                    if request.POST['promote'] == 'yes':
                        old_path = files[i] 
                        _, file_extension = os.path.splitext(old_path)
                        new_path = old_path.replace(file_extension,'.{}{}'.format(promotion_text_addition,file_extension))
                        os.rename(old_path,new_path)
                    this_file = files[i+1]
    except:
        this_file = None

    # begin response parsing
    url = this_file.replace(settings.BASE_DIR,'') if this_file is not None else this_file
    context = {
        'img': url,
        'dir': relative_dir,
        'i': idx,
        'promotion_text_addition': promotion_text_addition,
    }
    return HttpResponse(template.render(context, request))