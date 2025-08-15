import requests
from utils.config import load_token
from utils.config import API_BASE

def post_hack(data):
    token = load_token()
    if not token:
        raise Exception("❌ No token found. Run: 404cmd set --token ...")

    post_data = {"hackContent":data};
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(f"{API_BASE}/hacks", json=post_data, headers=headers)

    if res.status_code != 200:
        raise Exception(f"❌ Failed to push hack: {res.text}")

    return res.json()

def who_ami():
    token = load_token();
    if not token:
        raise Exception("❌ No token found. Run: 404cmd set --token ...")
    headers = {"Authorization":f"Bearer {token}"};

    res = requests.get(f"{API_BASE}/users/me",headers=headers);

    if res.status_code!=200:
       raise Exception(f"❌ Failed to fetch profile: {res.text}")
    
    return res.json();

def get_hack_by_id(hack_id):
    token = load_token()
    if not token:
        raise Exception("❌ No token found. Run: 404cmd set --token ...")
        
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    res = requests.get(f"{API_BASE}/hacks/{hack_id}/edit", headers=headers)

    if res.status_code != 200:
        raise Exception(f"Failed to read hack: {res.text}")
    return res.json()

def get_hack_by_slug(hack_slug):


    res = requests.get(
        f"{API_BASE}/hacks/{hack_slug}",
    )
    if res.status_code!=200:
        raise Exception(f"Failed to read hack: {res.text}")
    
    return res.json();


def update_hack_by_id(hack_id, parsed):
    token = load_token();
    if not token:
        raise Exception("No token found. Use: 404cmd set --token <token>")

    data = {"hackContent":parsed}

    res = requests.patch(
        f"{API_BASE}/hacks/{hack_id}",
        json=data,
        headers={"Authorization": f"Bearer {token}"}
    )
    if res.status_code != 200:
        raise Exception(f"Update failed: {res.status_code} — {res.text}")
    return res.json()

def search_hacks(tag,q,limit,page):

    SEARCH_URL = f"{API_BASE}/hacks/search";
    params = {};
    if(tag):
        params["tag"] = tag;
    if(q):
        params["q"] = q;
    if(limit):
        params["limit"]=limit;
    
    if(page):
        params["page"]=page;
    res = requests.get(
        SEARCH_URL,
        params=params
    )

    if res.status_code!=200:
        raise Exception(f"Update failed: {res.status_code} — {res.text}")
    
    return res.json();

def get_draft_hacks(page,limit):
    DRAFT_URL = f"{API_BASE}/hacks/drafts"
    token = load_token();
    if not token:
        raise Exception("No token found. Use: 404cmd set --token <token>")


    params = {};
    if(limit):
        params["limit"]=limit;
    
    if(page):
        params["page"] = page;

    res = requests.get(
        DRAFT_URL,
        params=params,
        headers={"Authorization": f"Bearer {token}"}
    )

    if res.status_code!=200:
       raise Exception(f"Draft failed: {res.status_code} — {res.text}")
    
    return res.json();




