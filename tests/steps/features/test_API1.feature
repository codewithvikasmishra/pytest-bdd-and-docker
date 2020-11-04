Feature: Passing parameters to API1

    Scenario Outline: Checking with pdf file
        when Execute the API with given <pdf_files> json where having 2 pdf file only
        Then response should be <code> for pdf
        Examples:
        |pdf_files|code|
        |/app/files/test1_pdf.json|200|

    Scenario Outline: Checking with multipartform/data
        when Execute the API1 with given <files> json with multipart content-type
        Then response should be <code> for multipart
        Examples:
        |files|code|
        |/app/files/test1_pdf.json|200|

    Scenario Outline: Check callback in API1
        when Execute the given <callback_files> in API1
        Then response should be <call_res> with parent and task id
        Examples:
        |callback_files|call_res|
        |/app/files/test1_pdf_callback.json|202|

    Scenario Outline: Check output schema of API1
        when Execute the given <Sch_files> in API1 to check schema
        Then response should be <boolean> for the given <schema>
        Examples:
        |Sch_files|boolean|schema|
        |/app/files/test1_pdf.json|True| Content-Type, X-Parsed-By,Content,create_date|

    Scenario Outline: Check with 400 status code
        when Execute API1 with blank file
        Then response should be <blank_res>
        Examples:
        |blank_res|
        |400|