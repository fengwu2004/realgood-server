import storemgr
from data.recommond_unit import ConsultorWithRecommonds, ConsultorRecommondsTrends
from analyse import calc_interval_amplitude_of_consultor

def doRun():

    consultors = storemgr.intance().loadConsultors()
    
    results = []
    
    for consultorWithRecoommond in consultors:
        
        temp = ConsultorRecommondsTrends()
    
        temp.consultor = consultorWithRecoommond.consultor
    
        temp.recommondsTrends = calc_interval_amplitude_of_consultor.doRun(consultorWithRecoommond.recommonds)
        
        results.append(temp.toJson())
        
    storemgr.intance().saveManyTo('recommondtrends', results)