from fastapi import APIRouter

router = APIRouter(prefix="/gitService")


@router.post("/")
def query_endpoint(request):
	return "hello world"