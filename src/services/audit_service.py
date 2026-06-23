from datetime import datetime

audit_logs = []

def log_action(action, patient_id, performed_by="system"):
    audit_logs.append({
        "action": action,
        "patient_id": patient_id,
        "performed_by": performed_by,
        "timestamp": datetime.now().isoformat()
    })