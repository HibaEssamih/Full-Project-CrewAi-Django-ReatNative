from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crewai import Crew
from .tasks import LegalQueryTasks
from .agents import LegalQueryAgents
import json


@csrf_exempt
def legal_assistance_check_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        # Initialize an empty list to store the chat history
        chat_history = []

        # Iterate over the keys in request.POST
        for key in request.POST:
            # Check if the key starts with 'history[' to identify history items
            if key.startswith('history['):
                # Get the values for this history item directly using the key
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                # Append the history item to the chat_history list
                chat_history.append(history_item)

        # Now chat_history contains all the chat history items as dictionaries
        print(chat_history)

        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            legal_assistance_checker_agent = agents.check_legal_assistance_agent()
            legal_assistance_check_task = tasks.check_legal_assistance_task(legal_assistance_checker_agent, query, chat_history)
            game = Crew(agents=[legal_assistance_checker_agent], tasks=[legal_assistance_check_task]).kickoff()

            # Check if `game` is a string
            if isinstance(game, str):
                if game.lower() in ["true", "yes"]:
                    return complex_tasks_view(request)
                elif game.lower() in ["false", "no"]:
                    return simple_query_analysis_view(request)
                else:
                    return JsonResponse({'error': 'Unknown result from legal assistance check'}, status=400)

            result = game  # Get the result directly

            if result.lower() in ["true", "yes"]:
                return complex_tasks_view(request)
            elif result.lower() in ["false", "no"]:
                return simple_query_analysis_view(request)
            else:
                return JsonResponse({'error': 'Unknown result from legal assistance check'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def document_generation_check_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            document_generation_checker_agent = agents.document_generation_check_agent()
            document_generation_check_task = tasks.document_generation_check_task(document_generation_checker_agent, query)

            crew = Crew(
                agents=[document_generation_checker_agent],
                tasks=[document_generation_check_task]
            )

            game = crew.kickoff()
            result = game  


            if result.lower() in ["true", "yes"]:
                return check_information_check_view(request)
            elif result.lower() in ["false", "no"]:
                return legal_assistance_check_view(request)
            else:
                return JsonResponse({'error': 'Unknown result from legal assistance check'}, status=400)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def check_information_check_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        chat_history = []

        for key in request.POST:
            if key.startswith('history['):
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                chat_history.append(history_item)

        
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            document_check_agent = agents.document_check_agent()
            check_information_task = tasks.check_information_task(document_check_agent, query, chat_history)

            crew = Crew(
                agents=[document_check_agent],
                tasks=[check_information_task]
            )

            game = crew.kickoff()
            result = game  


            if result.lower() in ["true", "yes"]:
                return document_generation_view(request)
            elif result.lower() in ["false", "no"]:
                return extract_information_for_document_generation_view(request)
            else:
                return JsonResponse({'error': 'Unknown result from legal assistance check'}, status=400)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def simple_query_analysis_view(request):
    print(request.POST)
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        
    
        chat_history = []

        # Iterate over the keys in request.POST
        for key in request.POST:
            # Check if the key starts with 'history[' to identify history items
            if key.startswith('history['):
                # Get the values for this history item directly using the key
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                # Append the history item to the chat_history list
                chat_history.append(history_item)

        # Now chat_history contains all the chat history items as dictionaries
        print(chat_history)


        
        print('hhhhhhhhhh', chat_history)
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            simple_query_agent = agents.simple_query_agent()
            simple_query_analysis = tasks.simple_query_analysis_task(simple_query_agent, query, chat_history)

            crew = Crew(
                agents=[simple_query_agent],
                tasks=[simple_query_analysis]
            )

            game = crew.kickoff()
            result = game  # The result is directly returned when the Crew game is kicked off

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def complex_tasks_view(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        query = request.POST.get('query', '')  
        # Initialize an empty list to store the chat history
        chat_history = []

        # Iterate over the keys in request.POST
        for key in request.POST:
            # Check if the key starts with 'history[' to identify history items
            if key.startswith('history['):
                # Get the values for this history item directly using the key
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                # Append the history item to the chat_history list
                chat_history.append(history_item)

        # Now chat_history contains all the chat history items as dictionaries
        print(chat_history)

        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            # Create Agents
            data_gathering_agent = agents.data_gathering_agent()
            nlp_agent = agents.natural_language_processing_agent()
            search_algorithm_agent = agents.search_algorithm_agent()
            legal_analysis_agent = agents.legal_analysis_agent()
            quality_assurance_agent = agents.quality_assurance_agent()
            report_generation_agent = agents.report_generation_agent()
            decision_maker_agent = agents.decision_maker_agent()


            # Create Tasks
            data_gathering = tasks.data_gathering_task(data_gathering_agent, query, chat_history)
            nlp_processing = tasks.natural_language_processing_task(nlp_agent, query, chat_history)
            search_algorithm = tasks.search_algorithm_task(search_algorithm_agent, query, chat_history)
            legal_analysis = tasks.legal_analysis_task(legal_analysis_agent, query, data_gathering.expected_output, chat_history)
            quality_assurance = tasks.quality_assurance_task(quality_assurance_agent, legal_analysis.expected_output)
            report_generation = tasks.report_generation_task(report_generation_agent, query, legal_analysis.expected_output, chat_history)
            decision_making = tasks.decision_making_task(decision_maker_agent, legal_analysis.expected_output, context=[legal_analysis, quality_assurance])


            # Set up task context
            legal_analysis.context = [data_gathering]
            quality_assurance.context = [legal_analysis]
            report_generation.context = [legal_analysis, quality_assurance]
            decision_making.context = [legal_analysis, quality_assurance]

            # Create Crew responsible for Legal Query
            crew = Crew(
                agents=[
                    data_gathering_agent,
                    nlp_agent,
                    search_algorithm_agent,
                    legal_analysis_agent,
                    quality_assurance_agent,
                    report_generation_agent,
                    decision_maker_agent,
                ],
                tasks=[
                    data_gathering,
                    nlp_processing,
                    search_algorithm,
                    legal_analysis,
                    quality_assurance,
                    report_generation,
                    decision_making,
                ]
            )

            # Start the crew's activities
            game = crew.kickoff()

            # Return results
            return JsonResponse({'result': str(game)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def extract_information_for_document_generation_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        chat_history = []

        for key in request.POST:
            if key.startswith('history['):
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                chat_history.append(history_item)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            document_generation_submission_agent = agents.document_generation_submission_agent()
            document_generation_submission_task = tasks.document_generation_submission_task(document_generation_submission_agent, query, chat_history)
            
            crew = Crew(
                agents=[document_generation_submission_agent],
                tasks=[document_generation_submission_task]
            )

            game = crew.kickoff()
            print('******************ttoo**********', str(game))

            return JsonResponse({'result': str(game)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def document_generation_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        chat_history = []

        for key in request.POST:
            if key.startswith('history['):
                history_item = {
                    'type': request.POST.get(key),
                    'text': request.POST.get(f'{key}[text]'),
                    'createdAt': request.POST.get(f'{key}[createdAt]')
                }
                chat_history.append(history_item)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            document_generation_agent = agents.document_generation_agent()
            document_generation_task = tasks.document_generation_task(document_generation_agent, query, chat_history)
            
            crew = Crew(
                agents=[document_generation_agent],
                tasks=[document_generation_task]
            )

            game = crew.kickoff()
            return JsonResponse({'document': str(game)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


