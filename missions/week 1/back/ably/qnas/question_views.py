import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

from qnas.models import Question, QuestionCategory
from products.models import Product
from core.decorators import login_required
from core.validators import validate_title, validate_content

class QuestionView(View):
    @login_required
    def post(self, request, product_id=None):
        try:
            
            if not product_id or not Product.objects.filter(id = product_id).exists():
                return JsonResponse({'messge' : 'Not Found'}, status = 404)
            
            data = json.loads(request.body)

            question_category_id = data['question_category_id']
            title = data['title']
            content = data['content']

            if not QuestionCategory.objects.filter(id = question_category_id).exists():
                return JsonResponse({'message' : 'Invalid Caterory'}, status = 400)
            validate_title(title)
            validate_content(content)

            Question.objects.create(
                user_id = request.user.id,
                product_id = product_id,
                question_category_id = question_category_id,
                title = title,
                content = content
            )

            return JsonResponse({'message' : 'Success'}, status = 201)

        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status = 400)
        except KeyError:
            return JsonResponse({'message' : 'Key Error'}, status = 400)
        except ValueError:
            return JsonResponse({'message' : 'Value Error'}, status = 400)