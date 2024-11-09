from django.http import JsonResponse
from .models import Project, Technology, Uses
import json
import logging
logger = logging.getLogger(__name__)


def projects_api(request):
    """Api for all projects and handles POST requests"""

    try:
        if request.method == "POST":
            # Create a project
            POST = json.loads(request.body)
            project = Project.objects.create(

                name=POST["name"],
                type=POST["type"],
                description=POST["description"],
                date=POST["date"],
                completed=POST["completed"]
            )
            return JsonResponse(project.as_dict(), status=201)

        return JsonResponse({
            # Return all projects handles GET requests
            'projects': [project.as_dict() for project \
                         in Project.objects.all()]
        })
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return JsonResponse({'error': str(e)}, status=400)


def technologies_api(request):
    """Api for all technologies and handles POST requests"""

    try:
        if request.method == "POST":
            # Create a technology
            POST = json.loads(request.body)
            technology = Technology.objects.create(
                name=POST["name"],
                type=POST["type"],
                description=POST["description"],
                version=POST["version"]
            )
            return JsonResponse(technology.as_dict(), status=201)

        return JsonResponse({
            # Return all technologies handles GET requests
            'technologies': [technology.as_dict() for technology in \
                             Technology.objects.all()]
        })
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return JsonResponse({'error': str(e)}, status=400)


def project_api(request, project_id):
    """Api for a single project and handles PUT and DELETE requests"""
    project = Project.objects.get(id=project_id)

    if request.method == "DELETE":
        # Delete a project
        project.delete()
        return JsonResponse({
            'message': 'Project deleted'
        })

    if request.method == "PUT":
        # Update a project
        PUT = json.loads(request.body)
        project.name = PUT["name"]
        project.type = PUT["type"]
        project.description = PUT["description"]
        project.date = PUT["date"]
        project.completed = PUT["completed"]
        project.save()
        return JsonResponse(project.as_dict())

    return JsonResponse(project.as_dict())


def technology_api(request, technology_id):
    """Api for a single technology and handles PUT and DELETE requests"""
    technology = Technology.objects.get(id=technology_id)

    if request.method == "DELETE":
        # Delete a technology
        technology.delete()
        return JsonResponse({
            'message': 'Technology deleted'
        })

    if request.method == "PUT":
        # Update a technology
        PUT = json.loads(request.body)
        technology.name = PUT["name"]
        technology.type = PUT["type"]
        technology.description = PUT["description"]
        technology.version = PUT["version"]
        technology.save()
        return JsonResponse(technology.as_dict())

    return JsonResponse(technology.as_dict())


def uses_api(request):
    """Api for all uses relationships and handles POST requests"""

    try:
        if request.method == "POST":
            # Create a uses relationship
            POST = json.loads(request.body)
            use = Uses.objects.create(
                technology=Technology.objects.get(id=str(POST["technology"])),
                project=Project.objects.get(id=str(POST["project"]))
            )
            return JsonResponse(use.as_dict(), status=201)
        # Return all uses relationships handles GET requests
        usesObj = {
            'uses': [use.as_dict() for use in Uses.objects.all()]
        }
        return JsonResponse(usesObj)
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return JsonResponse({'error': str(e)}, status=400)


def use_api(request, use_id):
    """Api for a single uses relationship, handles PUT and DELETE requests"""
    use = Uses.objects.get(id=use_id)

    if request.method == "DELETE":
        # Delete a uses relationship
        use.delete()
        return JsonResponse({
            'message': 'Use deleted'
        })

    if request.method == "PUT":
        # Update a uses relationship
        PUT = json.loads(request.body)
        use.technology = Technology.objects.get(id=str(PUT["technology"]))
        use.project = Project.objects.get(id=str(PUT["project"]))
        use.save()
        return JsonResponse(use.as_dict())

    return JsonResponse(use.as_dict())
