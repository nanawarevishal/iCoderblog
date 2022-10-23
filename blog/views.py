from asyncio.windows_events import NULL
from email import message
from unicodedata import name
from django.shortcuts import render,redirect,HttpResponse
from blog.models import blog,Category,blogComment,ContactUS,Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
import math,random
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.db.models import Q
import random
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def index(request):
    ls =[]
    allpost  = blog.objects.filter()
    for i in allpost:
        ls.append(i.views)
    ls.sort()
    ls.reverse()
    trending = blog.objects.filter(Q(views=ls[0]) | Q(views=ls[1]) | Q(views=ls[2]) | Q(views=ls[3]) | Q(views=ls[4]))
 
    obj = Category.objects.filter(cat_name__icontains ='Lifestyle')
    for i in obj:
        cat = i.cat_id
    
    lifestylepost = blog.objects.filter(cat_num__icontains = cat)

    #   Business Section

    b1 = blog.objects.filter(blog_id=4).first()
    b2 = blog.objects.filter(blog_id=3).first()
    b3 = blog.objects.filter(blog_id=12).first()

    business = blog.objects.filter(cat=1)

    # Lifestyle section

    l1 = blog.objects.filter(blog_id=15).first()
    l2 = blog.objects.filter(blog_id=16).first()
    l4 = blog.objects.filter(blog_id=8).first()
    l5 = blog.objects.filter(blog_id=9).first()
    l6 = blog.objects.filter(blog_id=13).first()

    lifestyle = blog.objects.filter(cat=5)

    # Travel blog

    t1 = blog.objects.filter(blog_id=6).first()
    t2 = blog.objects.filter(blog_id=7).first()


    # Technology blog

    tc1 = blog.objects.filter(blog_id=14).first()
    tc2 = blog.objects.filter(blog_id=5).first()

    #Culture blog

    c1 = blog.objects.filter(blog_id=17).first()
    c2 = blog.objects.filter(blog_id=18).first()
    c3 = blog.objects.filter(blog_id=19).first()
    c4 = blog.objects.filter(blog_id=20).first()
    c5 = blog.objects.filter(blog_id=21).first()

    culture_post = blog.objects.filter(cat=6)

    param = {'allpost':allpost,'lifestylepost':lifestylepost,'trending':trending,'b1':b1,'business':business,'b2':b2 ,'b3':b3,'l1':l1,'l2':l2,'l4':l4,'l5':l5,'l6':l6,'t1':t1,'t2':t2,'tc1':tc1,'tc2':tc2,'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'lifestyle':lifestyle,'culture_post':culture_post}

    return render(request,'index.html',param)


def about(request):
    return render(request,'about.html')

def single_post(request,blogID=0):

    # TRENDING SECTION
    ls = []
    lst = []
    blogp = blog.objects.all()
    for i in blogp:
        ls.append(i.views)
        lst.append(i.date)
    ls.sort()
    lst.sort()
    ls.reverse()
    lst.reverse()
    trending = blog.objects.filter(Q(views=ls[0]) | Q(views=ls[1]) | Q(views=ls[2]) | Q(views=ls[3]) | Q(views=ls[4]))

     # RECENT SECTION
     # RECENT SECTION
    latest = blog.objects.filter(Q(date=lst[0]) | Q(date=lst[1]) | Q(date=lst[2]) | Q(date=lst[3]) | Q(date=lst[4]))


    blogpost={}
    if blogID:
        blogpost = blog.objects.filter(blog_id__icontains=blogID)
        
   

    post = blog.objects.filter(blog_id=blogID).first()
    post.views = post.views + 1
    post.save()
    comments= blogComment.objects.filter(post=post, parent=None)
    replies= blogComment.objects.filter(post=post).exclude(parent=None)
    blogtag = blog.objects.filter()

    tag = []
    for i in blogtag:
        tag.append(i.tags)

    print(tag)
        
    catName = Category.objects.all()
    param = {'catName':catName,'blogtag':blogtag,'blogpost':blogpost,'comments':comments,'trendings':trending,'latest':latest}
    return render(request,'single-post.html',param)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= blog.objects.get(blog_id=postSno)
        # parentSno= request.POST.get('parentSno')
        if comment=="":
            messages.warning(request, "Please enter the comment....!")


        else:
            comment=blogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")

        # else:
        #     parent = blogComment.objects.get(sno = parentSno)
        #     comment=blogComment(comment= comment, user=user, post=post,parent=parent)
        #     comment.save()
        #     messages.success(request, "Your replay has been posted successfully")

        
        return redirect(f"singlepost/{post.blog_id}")

def category(request,catno=0,tags=NULL):
    if catno:
        catName = Category.objects.all()
        catnm = Category.objects.filter(cat_id=catno).first()
        blogpost = blog.objects.filter(cat=catno).order_by('date').reverse()

        paginator = Paginator(blogpost,2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


         # TRENDING SECTION
        ls = []
        lst=[]
        blogp = blog.objects.all()
        for i in blogp:
            ls.append(i.views)
            lst.append(i.date)
        ls.sort()
        lst.sort()
        ls.reverse()
        lst.reverse()
        trending = blog.objects.filter(Q(views=ls[0]) | Q(views=ls[1]) | Q(views=ls[2]) | Q(views=ls[3]) | Q(views=ls[4])).order_by('views').reverse()

        # RECENT SECTION
        latest = blog.objects.filter(Q(date=lst[0]) | Q(date=lst[1]) | Q(date=lst[2]) | Q(date=lst[3]) | Q(date=lst[4])).order_by('date').reverse()


        blogtag = blog.objects.all() 
        param = {'blogpost':blogpost,'catName':catName,'blogtag':blogtag,'trendings':trending,'latest':latest,'catnm':catnm,'page_obj':page_obj}
        return render(request,'category.html',param)


    if tags:
        catName = Category.objects.all()
        blogtag = blog.objects.all()
        blogpost = blog.objects.filter(tags__icontains=tags)
        param = {'blogpost':blogpost,'catName':catName,'blogtag':blogtag}
        return render(request,'category.html',param)

   
    
def tags(request,tags=NULL):
    if tags:
        catName = Category.objects.all()
        blogpost = blog.objects.filter(tags__icontains=tags)
        param = {'blogpost':blogpost,'catName':catName}
    return render(request,'category.html',param)


def Signup(request):
    if request.method =="POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        mobile = request.POST['mobile_no']
       
        try:
            if User.objects.filter(username=username).first():
                messages.warning(request,"Username is taken..!")
                return redirect('index')

            if User.objects.filter(email=email).first():
                messages.warning(request,"Email is already taken...!")
                return redirect('index')

            if password != confirm_pass:
                messages.warning(request,"Password did not match....!")
                return redirect("index")

            user_obj = User.objects.create(username=username,password = password)
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.set_password(password)
            user_obj.save()

            global otp
            otp = generateOTP()

            global auth_token
            auth_token = str(uuid.uuid4())

            profile_obj = Profile(user = username,auth_token=auth_token,first_name=first_name,last_name=last_name,email=email,mobile_no = mobile)
            sendEmail(email,otp,auth_token)
            messages.success(request,"Please check your mail....! and verify your OTP..!")
            profile_obj.save()
            return redirect("sendotp")
        
        except Exception as e:
            print(e)
            return redirect('index')

    else:
        return render(request,'Signup.html')          
        

def Login(request):
    if request.method=='POST':
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername,password=loginpassword)

        profile_obj = Profile.objects.filter(user = loginusername).first()

        if not profile_obj.is_verified :
            messages.warning(request,"Please verify the account....!")
            return render(request,"login.html")

        if user is not None:
            login(request,user)
            messages.success(request,"You are successfully login...!")
            return redirect ('index')

        else:
            messages.warning(request,"invalid credential ...! Enter correct credentials..!")
            return redirect('index')

    else:
        return render(request,'Login.html')
    

def logoutuser(request):
    logout(request)
    messages.success(request,"You are successfully logout....!")
    return redirect('index')


def sendEmail(email,otp,token):
    subject = "Your account need to be verified"
    msg = f"hi paste your link http://127.0.0.1:8000/otp/{token} \n\n Your OTP is: {otp}\n\nDo not share your OTP with any one"

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,msg,email_from,recipient_list)
    

# def verify(request,auth_token):
    # try:
    #     profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    #     # print(profile_obj)
    #     if profile_obj:
    #         if profile_obj.is_verified:
    #             messages.success(request,"Your account is already verified....!")
    #             return redirect('login')

    #         profile_obj.is_verified=True
    #         profile_obj.save()
    #         messages.success(request,"Congratulations Your email has been verified....!")
    #         return redirect('login')


    # except Exception as e:
    #     print(e)        


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def sendotp(request):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    param={'profile_obj':profile_obj}
    return render(request,'sendotp.html',param)



def otp(request,auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj.is_verified:
        messages.success(request,"Your account has been already verified.....!")
        return render(request,'login.html')

    else:
        if request.method=="POST":
            otp1 = request.POST["OTP"]
        
            if otp1==otp:
                messages.success(request,"Your otp has been verified successfully....!")
                profile_obj.is_verified = True
                profile_obj.save()
                return redirect('login')

            else:
                messages.warning(request,"OTP did not matched please try again...!")
                return render(request,'sendotp.html')


def search(request):
    if request.method == "POST":
        query = request.POST['search']
        print(query)

        if len(query)>78 or query=='':
            allPost = blog.objects.none()
    
        else:
            allPosttitle = blog.objects.filter(title__icontains=query)
            allPostcontent = blog.objects.filter(blog_info__icontains=query)
            allPost = allPosttitle.union(allPostcontent)
            print(allPost)

        if allPost.count() == 0 :
            messages.warning(request,"No search result found...!")

    
    
    # TRENDING SECTION
    ls = []
    blogp = blog.objects.all()
    for i in blogp:
        ls.append(i.views)
    ls.sort()
    ls.reverse()
    trending = blog.objects.filter(Q(views=ls[0]) | Q(views=ls[1]) | Q(views=ls[2]) | Q(views=ls[3]) | Q(views=ls[4]))

    # RECENT SECTION
    latest = blog.objects.filter(date__range=["2022-09-01", "2022-10-31"])


    params = {'allPost':allPost,'query':query,'trendings':trending,'latest':latest}
    
    return render (request,'search-result.html',params)


def profile(request):
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mobile_no= request.POST['mobile_no']
        email = request.POST['email']
        profile_image = request.FILES['profile_image']

        prfile_obj= Profile(first_name=fname,last_name=lname,mobile_no=mobile_no,email=email,profile_img=profile_image,user=username)
        prfile_obj.save()
        messages.success(request,"Congratulations your profile has been updated successfully.......!")
    

    return render(request,'profile.html')


def contactus(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']


        if len(msg) < 0 or len(sub) < 0:
            messages.warning(request,'Please enter all the fields....!')
            return render(request,'contact.html')

        else:
            contactOBJ = ContactUS(name=name,email=email,subject=sub,msg=msg)
            contactOBJ.save()
            messages.success(request,'Your message sent succefully......!')
            return render(request,'contact.html')

    return render(request,'contact.html')
