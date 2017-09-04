import storemgr
from data.recommond_unit import ConsultorWithRecommonds, ConsultorRecommondsTrends
from analyse import calc_interval_amplitude_of_consultor

consultors = storemgr.intance().loadConsultors()

results = []

for consultorWithRecoommond in consultors:
    
    temp = ConsultorRecommondsTrends()

    temp.consultor = consultorWithRecoommond.consultor
    
    for item in consultorWithRecoommond.recommonds:
        
        pass