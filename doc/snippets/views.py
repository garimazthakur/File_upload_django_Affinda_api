from affinda import AffindaAPI, TokenCredential
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import AffindaSerializer
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Snippet, Affinda

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

class CreateSnippet(APIView):
    def post(self, request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SnippetDetail(APIView):
   
    def get_object(self,request,  pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

class GetSnippetDetails(APIView):
    def get(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer=SnippetSerializer(snippet)
            print(serializer.data)
            return Response(serializer.data)
        except:
            raise Http404

class UpdateSnippetDetail(APIView):
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
        
class DeleteSnippetDetail(APIView):
    def delete(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            snippet.delete()
            return Response({"message":"The id {pk} is deleted"})
        except Snippet.DoesNotExist:
            return Response({"message": "Snippet does not exist"})
class AffindaNER(APIView):
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

            # print(serializer)
            # print(serializer.data['file'])
            file_path = Affinda.objects.get(id=int(data.id)).file
            print(file_path)
            print("-------------------")

            #other way to get filepath
            # folder=  os.path.join((os.path.dirname(os.path.dirname((__file__)))), 'affinda_files')
            # print(folder)
            # myfile = Affinda(file= request.FILES['file'])
            # x = str(myfile.file.name)
            # print(type(x))
            # file_path=  os.path.join(folder, x)
            # print("<<<<<<<<<<<<---------------------------------------------------------------------->>>>>>>>>>")
            with open((file_path), "rb") as f:
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
