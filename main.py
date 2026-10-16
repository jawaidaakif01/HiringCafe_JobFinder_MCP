import asyncio
from job_search import search_jobs
from job_details import get_job_details

async def main():
    print("=" * 45)
    print("      HIRINGCAFE JOB FINDER")
    print("=" * 45)

    query = input(
        "\nEnter job title (default: AI/ML Engineer): "
    ).strip() or "AI/ML Engineer"

    location = input(
        "Enter location (default: India): "
    ).strip()

    print("\nEmployment type: ")
    print("1. Internship")
    print("2. Full Time")
    print("3. Contract")
    print("4. Any")

    choices = {
        "1" : "Internship",
        "2" : "Full Time",
        "3" : "Contract",
        "4" : "Any",
    }

    choice = input("Choose 1-4 (default: 1): ").strip() or "1"

    if choice not in choices:
        print("Invalid choice. Using Internship.")
        choice = "1"

    employment_type = choices[choice]

    limit_input = input(
        "\nNumber of jobs, 1-25 (default: 10): "
    ).strip()

    try:
        limit = int(limit_input) if limit_input else 10
        if not 1 <= limit <= 25:
            raise ValueError
    except ValueError:
        print("Invalid limit. Using 10.")
        limit = 10

    print("\nSearching HiringCafe...")
    print("-" * 45)


    try:
        search_query = query

        if employment_type == "Internship":
            search_query = f"{query} intern internship"

        jobs = await search_jobs(
            query=search_query,
            location=location,
            employment_type=employment_type,
            limit=limit
        )

        if not jobs:
            print("No jobs were returned for this search.")
            return

        print(f"\nFound {len(jobs)} jobs(s):\n")

        for index, job in enumerate(jobs, start=1):
            print(f"{index}. {job['title']}")
            print(f"    Company: {job['company'] or 'Not provided'}")
            print(f"    Location: {job['location'] or 'Not provided'}")
            print(f"    Workplace: {job['workplace'] or 'Not provided'}")
            print(f"    Salary: {job['compensation'] or 'Not provided'}")
            print(f"    Employment: {job['employment_type'] or 'Not provided'}")
            print(f"    Apply: {job['url'] or 'Not provided'}")

        selected = input(
            "\nEnter a job number to view full details "
            "(or press Enter to exit): "
        ).strip()

        if selected:
            try:
                index = int(selected) - 1

                if not 0 <= index < len(jobs):
                    print("Invalid job number.")
                    return

                job_id = jobs[index].get("job_id")

                if not job_id:
                    print("Job ID is missing for this listing.")
                    return

                print("\nFetching full job details...\n")

                details = await get_job_details(job_id)
                print(details)

            except ValueError:
                print("Please enter a valid numbe.")

    except Exception as error:
        print(f"\nSomething went wrong: {error}")



if __name__=="__main__":
    asyncio.run(main())