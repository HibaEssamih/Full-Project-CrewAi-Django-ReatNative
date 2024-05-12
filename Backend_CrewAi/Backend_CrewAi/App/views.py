from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crewai import Crew
from .tasks import LegalQueryTasks
from .agents import LegalQueryAgents

@csrf_exempt
def legal_assistance_check_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            legal_assistance_checker_agent = agents.check_legal_assistance_agent()
            legal_assistance_check_task = tasks.check_legal_assistance_task(legal_assistance_checker_agent, query)
            game = Crew(agents=[legal_assistance_checker_agent], tasks=[legal_assistance_check_task]).kickoff()

            # Check if `game` is a string
            if isinstance(game, str):
                if game.lower() in ["true", "yes"]:
                    return complex_tasks_view(request)
                elif game.lower() in ["false", "no"]:
                    return simple_query_analysis_view(request)
                else:
                    return JsonResponse({'error': 'Unknown result from legal assistance check'}, status=400)

            # Assuming `game` is a Crew object
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
def simple_query_analysis_view(request):
    print(request.POST)
    if request.method == 'POST':
        query = request.POST.get('query', '')  
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            simple_query_agent = agents.simple_query_agent()
            simple_query_analysis = tasks.simple_query_analysis_task(simple_query_agent, query)

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
            data_gathering = tasks.data_gathering_task(data_gathering_agent, query)
            nlp_processing = tasks.natural_language_processing_task(nlp_agent, query)
            search_algorithm = tasks.search_algorithm_task(search_algorithm_agent, query)
            legal_analysis = tasks.legal_analysis_task(legal_analysis_agent, query, data_gathering.expected_output)
            quality_assurance = tasks.quality_assurance_task(quality_assurance_agent, legal_analysis.expected_output)
            report_generation = tasks.report_generation_task(report_generation_agent, query, legal_analysis.expected_output)
            decision_making = tasks.decision_making_task(decision_maker_agent, legal_analysis.expected_output, context=[legal_analysis, quality_assurance])


            # Set up task context
            legal_analysis.context = [data_gathering]
            quality_assurance.context = [legal_analysis]
            report_generation.context = [legal_analysis, quality_assurance]

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