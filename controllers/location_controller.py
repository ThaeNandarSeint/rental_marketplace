from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.location_schema import CreateLocation, GetLocationsDto, GetLocationsResponse, UpdateLocation, Location
from usecases.location_usecase import LocationUseCase

router = APIRouter(prefix="/locations", tags=["locations"])

def get_usecase():
    return LocationUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetLocationsDto:
    return GetLocationsDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetLocationsResponse)
def get_locations(queries: GetLocationsDto = Depends(get_queries),usecase: LocationUseCase = Depends(get_usecase)):
    return usecase.get_locations(queries)

@router.get("/{id}", response_model=Location)
def get_location(id: int, usecase: LocationUseCase = Depends(get_usecase)):
    return usecase.get_location_by_id(id)

@router.post("/", response_model=Location)
def create_location(data: CreateLocation, usecase: LocationUseCase = Depends(get_usecase)):
    return usecase.create_location(data)

@router.patch("/{id}", response_model=Location)
def update_location(id: int, data: UpdateLocation, usecase: LocationUseCase = Depends(get_usecase)):
    return usecase.update_location(id, data)

@router.delete("/{id}", response_model=Location)
def delete_location(id: int, usecase: LocationUseCase = Depends(get_usecase)):
    return usecase.delete_location(id)
