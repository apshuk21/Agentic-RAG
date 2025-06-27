from langchain_core.prompts import PromptTemplate

prompts = {
    'grading_prompt': PromptTemplate.from_template(
    """
        You are a grader deciding if a document is relevant to a user’s question.
        Here is the document: {context}
        Here is the user’s question: {question}
        If the document talks about or contains information related to the user’s question, mark it as relevant. 
        Give a 'YES' or 'NO' answer to show if the document is relevant to the question.
    """
    ),
    'query_rewriter_prompt': PromptTemplate.from_template(
    """
        Look at the user_query and try to reason about the underlying semantic intent or meaning. 
        Here is the user query: {question} 
        Formulate an improved question:
    """
    )
}