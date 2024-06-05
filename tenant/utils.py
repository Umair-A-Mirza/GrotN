from .models import Swipe
from .models import Match

from landlord.models import House
from landlord.models import Housing

def update_match(swipe): 
    tenant = swipe.tenant
    partner = swipe.partner
    matching_swipe = Swipe.objects.filter(tenant=partner, partner=tenant).first()
    if not matching_swipe: 
        return

    existing_match = Match.objects.filter(tenant1=tenant, tenant2=partner).first()
    if not existing_match: 
        existing_match = Match.objects.filter(tenant1=partner, tenant2=tenant).first()
    
    if existing_match: 
        if matching_swipe.status and swipe.status: 
            existing_match.status = True
        else: 
            existing_match.status = False

        existing_match.save()
        return existing_match

    match = Match(tenant1=tenant, tenant2=partner, status=matching_swipe.status and swipe.status)
    match.save()

    return match


def update_housing(match):
    print("Updating housing for match", match)

    available_houses = House.objects.filter(price__lte=match.budget+match.budget*0.2)
    print("Available houses", available_houses)
    for available_house in available_houses:
        if available_house.city in match.city: 
            pass

        # if an housing already exists between the match and the house
        existing_housing = Housing.objects.filter(tenants=match, house=available_house).first()
        if existing_housing and not match.status: 
            existing_housing.is_active = False
            existing_housing.save()
            continue
        elif existing_housing: 
            existing_housing.is_active = True
            existing_housing.save()
            continue
        
        # creating a new housing with the available house and the match
        housing = Housing(tenants=match, house=available_house)
        housing.save()