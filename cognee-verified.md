Confirmed working Cognee setup (Gemini-backed):

\- LLM\_PROVIDER=gemini, LLM\_MODEL=gemini/gemini-2.5-flash

\- EMBEDDING\_PROVIDER=gemini, EMBEDDING\_MODEL=gemini/gemini-embedding-001, EMBEDDING\_DIMENSIONS=3072

\- ENABLE\_BACKEND\_ACCESS\_CONTROL and REQUIRE\_AUTHENTICATION must be set to "false" BEFORE importing cognee



Confirmed working calls:

\- cognee.remember(content, session\_id=customer\_id) -> session memory

\- cognee.remember(content, dataset\_name=dataset) -> permanent graph memory (per-customer dataset)

\- cognee.recall(query, session\_id=customer\_id) -> returns graph completion results

\- cognee.improve(dataset\_name=dataset) -> enriches the graph

\- cognee.forget(dataset=dataset) -> deletes a dataset (errors if dataset doesn't exist yet)



Pattern used: each customer gets their own dataset "customer\_{customer\_id}"

for isolation, so /forget for one customer doesn't affect others.

