from datetime import datetime

audit_logs = []

def log_action(action, patient_id):
    audit_logs.append({
        "action": action,
        "patient_id": patient_id,
        "timestamp": datetime.now().isoformat()
    })