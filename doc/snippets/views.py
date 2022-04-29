# from rest_framework import generics, permissions
from affinda import AffindaAPI, TokenCredential
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Snippet, Affinda
from email import message
from django.conf import settings
import os
class SnippetList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    def get(self, request, format=None):
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

class CreateSnippet(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    def get_object(self,request,  pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    # def get(self, request, pk, format=None):
    #     snippet=self.get_object(pk)
    #     serializer=SnippetSerializer(snippet)
    #     return Response(serializer.data)
class GetSnippetDetails(APIView):
    def get(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer=SnippetSerializer(snippet)
            print(serializer.data)
            print("****************************************************************")

            return Response(serializer.data)
        except:
            raise Http404

class UpdateSnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]      
    def put(self, request, pk,format=None):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer= SnippetSerializer(snippet, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Snippet.DoesNotExist:
            return Response({"message": "Snippet does not exist"})
        


            # snippet=self.get_object(pk)
            # serializer= SnippetSerializer(snippet, data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteSnippetDetail(APIView):
    def delete(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            snippet.delete()
            return Response({"message":"The id {pk} is deleted"})
        except Snippet.DoesNotExist:
            return Response({"message": "Snippet does not exist"})
    # def get_object(self,request,  pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset=User.objects.all()
#     serializer_class= UserSerializer
from .serializers import AffindaSerializer

class AffindaNER(APIView):
    # def post(self,request ):
    #     # if request.method == 'POST':
    #     if 'file' not in request.FILES:
    #         return Response({"message": 'No file provided/Check the key, spelling or any space after or in the key.'})
    #     file = request.FILES['file']
    #     print('---------------------->>')
    #     print(file)
    #     # if file.filename == '':
    #     #     return Response({"message": 'No file selected.'})
    #     #try this idea: https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/

        # token = "882cef4ed52c12069650b808d49bde924b5252c4"
        # credential = TokenCredential(token=token)
        # client = AffindaAPI(credential=credential)
    #     # print(file.filename)
    #     # for filename, file in request.FILES.iteritems():
    #     #     x= request.FILES[filename]
    #     #     name = request.FILES[filename].name
    #     # print(name)
    #     print("*******************************************************")
    #     # print(x)

    #     print("*******************************************************")

    #     folder= os.path.join(UPLOAD_FOLDER, file.filename)
    #     print(folder)
    #     with open('file', "rb") as f:
    #         resume = client.create_resume(file=f)
    #         data = resume.as_dict()
        # return Response({"data": data})

    def post(self, request):

        data = request.data
        token = "882cef4ed52c12069650b808d49bde924b5252c4"
        credential = TokenCredential(token=token)
        client = AffindaAPI(credential=credential)
        
        
        serializer = AffindaSerializer(
            data=data,
        )
        if serializer.is_valid():
            data = serializer.save()
            print("-------------------")
            print(data.id)
            file_path = Affinda.objects.get(id=int(data.id)).file
            print(file_path)
            print("-------------------")

            # print(serializer)
            # print(serializer.data['file'])
            # print("**************************************************************************")
            # # print(os.path.dirname(os.path.dirname((__file__))))
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # folder=  os.path.join((os.path.dirname(os.path.dirname((__file__)))), 'affinda_files')
            # print(folder)
            # myfile = Affinda(file= request.FILES['file'])
            # x = str(myfile.file.name)
            # print(type(x))
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                        
            # output=  os.path.join(folder, x)
            # print(output)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #    /home/softuvo/Garima/CRUD_Django/doc/affinda_files/yogita_rani_php.pdf

            
            # my_path= os.path.join(base_dir, "" )
            # my_path = r"base_dir/affinda_files/yogita_rani_php.pdf"
            # print(file_dir)
            # print("<<<<<<<<<<<<---------------------------------------------------------------------->>>>>>>>>>")
            with open(str(file_path), "rb") as f:
                resume = client.create_resume(file=f)
                data = resume.as_dict()
            return Response(
                {
                    "data": data,
                    "code": status.HTTP_200_OK,
                    "message": "Media created successfully",
                }
            )
        else:
            return Response(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "serializer errors",
                }
            )