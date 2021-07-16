import streamlit as st
import streamlit.components.v1 as components

import re

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('punkt')

#functions section

#function for list to string
def listToString(s): 
    # initialize an empty string
    str1 = " " 
    return (str1.join(s))

#civil cases section
property_keywords = ['property','house', 'real estate','condo','mansion','land']
sales_keywords = ['sale', 'barter']
succession_keywords = ['succession']
agency_keywords = ['agency','agent']
partnership_keywords = ['partnership','partner'] 
second_civil_keywords = {
    'is_property': property_keywords,
    'is_sales': sales_keywords,
    'is_succession':succession_keywords,
    'is_agency': agency_keywords,
    'is_partnership': partnership_keywords
}
civil_dict_intent = {intent: re.compile('|'.join(keys)) for intent, keys in second_civil_keywords.items()}
def civil_context(cust_input):
    for intent, pattern in civil_dict_intent.items():
        if re.search(pattern, cust_input): 
            return(intent)
    else:
        return('generic')

second_civil_dict_response = {
    'is_property': 'property case',
    'is_sales': 'sales case',
    'is_succession':'succession case',
    'is_agency': 'agency case',
    'is_partnership': 'partnership case'
    }
def second_civil_answer(text):
    response = second_civil_dict_response.get(civil_context(text))
    return response

#commercial cases section
negotiable_instruments_keywords = ['bank check','promissory']
corporation_keywords = ['corporation','corporate','incorporate','stock holder','investment']
second_commercial_keywords = {
    'is_negotiable_instruments': negotiable_instruments_keywords,
    'is_corporation':corporation_keywords
    }
commercial_dict_intent = {intent: re.compile('|'.join(keys)) for intent, keys in second_commercial_keywords.items()}
def commercial_context(cust_input):
    for intent, pattern in commercial_dict_intent.items():
        if re.search(pattern, cust_input): 
            return(intent)
    else:
        return('generic')
second_commercial_dict_response = {
    'is_negotiable_instruments': 'negotiable instrument case',
    'is_corporation': 'corporation case',
}
def second_commercial_answer(text):
    response = second_commercial_dict_response.get(commercial_context(text))
    return response

#criminal cases section
national_security_keywords = ['treason','espionage','piracy']
fundamental_laws_keywords = ['rebellion','coup etat','sedition','disorder']
public_interest_keywords = ['counterfeit','falsification']
against_person_keywords = ['homicide','murder','injury','rape','kidnap']
against_property_keywords = ['robbery','theft']
second_criminal_keywords = {
    'is_national_security': national_security_keywords,
    'is_fundamental_laws':fundamental_laws_keywords,
    'is_public_interest':public_interest_keywords,
    'is_against_person':against_person_keywords,
    'is_against_property':against_property_keywords
}
criminal_dict_intent = {intent: re.compile('|'.join(keys)) for intent, keys in second_criminal_keywords.items()}
def criminal_context(cust_input):
    for intent, pattern in criminal_dict_intent.items():
        if re.search(pattern, cust_input): 
            return(intent)
    else:
        return('generic')

second_criminal_dict_response = {
    'is_national_security': 'national security case',
    'is_fundamental_laws':'fundamental laws case',
    'is_public_interest':'public interest case',
    'is_against_person':'against person case',
    'is_against_property':'against property case'
    }
def second_criminal_answer(text):
    response = second_criminal_dict_response.get(criminal_context(text))
    return response

#labor cases section
employment_keywords = ['employ','employment','employee','recruit','recruitment']
work_keywords = ['work','holiday','paternity','maternity','conditions','retire']
benefits_keywords = ['pay','benefit','wage','coverage','insurance']
union_keywords = ['union','collective','association']
second_labor_keywords = {
    'is_employment':employment_keywords,
    'is_work':work_keywords,
    'is_benefit':benefits_keywords,
    'is_union':union_keywords
    }
labor_dict_intent = {intent: re.compile('|'.join(keys)) for intent, keys in second_labor_keywords.items()}
def labor_context(cust_input):
    for intent, pattern in labor_dict_intent.items():
        if re.search(pattern, cust_input): 
            return(intent)
    else:
        return('generic')

second_labor_dict_response = {
    'is_employment':'employment case',
    'is_work':'work case',
    'is_benefits':'benefits case',
    'is_union':'union case'
}
def second_labor_answer(text):
    response = second_labor_dict_response.get(labor_context(text))
    return response

#tax cases section
income_tax_keywords = ['income','estate','business','earnings']
indirect_tax_keywords = ['VAT']
excise_tax_keywords = ['excise','valorem','tobacco','alcohol','petroleum','mining']
stamp_tax_keywords = ['documentary','stamp','dividend','certificate','bonds','insurance','receipt','mortgage']
external_tax_keywords = ['customs','tariff']
second_tax_keywords = {
    'is_income_tax':income_tax_keywords,
    'is_indirect_tax':indirect_tax_keywords,
    'is_excise_tax':excise_tax_keywords,
    'is_stamp_tax':stamp_tax_keywords,
    'is_external_tax':external_tax_keywords,
}
tax_dict_intent = {intent: re.compile('|'.join(keys)) for intent, keys in second_tax_keywords.items()}
def tax_context(cust_input):
    for intent, pattern in tax_dict_intent.items():
        if re.search(pattern, cust_input): 
            return(intent)
    else:
        return('generic')
second_tax_dict_response = {
    'is_income_tax':'income tax case',
    'is_indirect_tax':'indirect tax case',
    'is_excise_tax':'excise tax case',
    'is_stamp_tax':'stamp tax case',
    'is_external_tax':'external tax case'
}
def second_tax_answer(text):
    response = second_tax_dict_response.get(tax_context(text))
    return response



#streamlit section
my_page = st.sidebar.radio('Sprint Navigation', ['Introduction','Demo'])#,'Data','How It Works','Demo','Contributors'])

if my_page == 'Introduction':
    st.title("Introduction")
    
    st.header("Problem Statement")
#     st.image(banner)
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
    st.header("Objectives")
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
    st.header("Use - Cases")
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
# elif my_page == 'Data':
#     st.title("The Dataset")
    
#     st.header("Sources")
    
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
#     st.header("Web Scraping")
    
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
    
#     st.header("Data Cleaning")
    
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)

    
# elif my_page == 'How It Works':
#     st.title("Topic Modeling")
    
#     st.header("Bag of Words")
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
    
#     st.header("IDF")
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)
    
#     st.header("LDA")
#     st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque varius dolor vel dolor tempus, vel gravida lorem finibus. Integer placerat placerat dolor, non lacinia lectus. Ut et dolor ultrices, viverra nibh non, laoreet leo. Ut sed mi in risus aliquam accumsan sit amet at nisl. Etiam tempus sapien ante, mattis rhoncus elit elementum vitae. Morbi eget lacus nec nibh ultrices varius eget sit amet nibh. Donec aliquam nunc sit amet sagittis consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam purus tellus, bibendum et condimentum pellentesque, efficitur non nisl. Curabitur cursus maximus est ut malesuada. Vestibulum ultricies sollicitudin dapibus. Morbi a sollicitudin elit, eu varius ligula. Pellentesque at semper nisl, at placerat lacus.',unsafe_allow_html=False)


elif my_page == 'Demo':
    st.title("Court Case Analyzer")
    st.markdown('This short demo allows us to analyze a new case and see which category it is mostly associated with.',unsafe_allow_html=False)
    
    st.write("Check out these supreme court [cases](https://lawphil.net/judjuris/judjuris.html) to test out in the Court Case Analyzer")

    user_input = st.text_input("submit your case text here")
    
    sentence_list = nltk.tokenize.sent_tokenize(user_input)
    
    lmtzr = WordNetLemmatizer()
    lemmatized = [[lmtzr.lemmatize(word) for word in word_tokenize(s)] for s in sentence_list]
    lemma_str_sentences = [listToString(s) for s in lemmatized]
    
# civil analyzing
    second_civil_answer_per_sentences = [second_civil_answer(x) for x in lemma_str_sentences]
    property_counts = second_civil_answer_per_sentences.count('property case')
    sales_counts = second_civil_answer_per_sentences.count('sales case')
    succession_counts = second_civil_answer_per_sentences.count('succession case')
    agency_counts = second_civil_answer_per_sentences.count('agency case')
    partnership_counts = second_civil_answer_per_sentences.count('partnership case')
    second_civil_total_counts = {
        property_counts:'property case',
        sales_counts: 'sales case',
        succession_counts:'succession case',
        agency_counts:'agency case',
        partnership_counts:'partnership case'
        }
    temp_civil = max(second_civil_total_counts)
    
# commercial analyzing
    second_commercial_answer_per_sentences = [second_commercial_answer(x) for x in lemma_str_sentences]
    negotiable_instruments_counts = second_commercial_answer_per_sentences.count('negotiable instrument case')
    corporation_counts = second_commercial_answer_per_sentences.count('corporation case')
    second_commercial_total_counts = {
        negotiable_instruments_counts:'negotiable instrument case',
        corporation_counts: 'corporation case',
        }
    temp_commercial = max(second_commercial_total_counts)

# criminal analyzing
    second_criminal_answer_per_sentences = [second_criminal_answer(x) for x in lemma_str_sentences]
    national_security_counts = second_criminal_answer_per_sentences.count('national security case')
    fundamental_laws_counts = second_criminal_answer_per_sentences.count('fundamental laws case')
    public_interest_counts = second_criminal_answer_per_sentences.count('public interest case')
    against_person_counts = second_criminal_answer_per_sentences.count('against person case')
    against_roperty_counts = second_criminal_answer_per_sentences.count('against property case')
    second_criminal_total_counts = {
        national_security_counts:'national security case',
        fundamental_laws_counts:'fundamental laws case',
        public_interest_counts:'public interest case',
        against_person_counts:'against person case',
        against_roperty_counts:'against property case'
        }
    temp_criminal = max(second_criminal_total_counts)
    
# labor analyzing
    second_labor_answer_per_sentences = [second_labor_answer(x) for x in lemma_str_sentences]
    employment_counts = second_labor_answer_per_sentences.count('employment case')
    work_counts = second_labor_answer_per_sentences.count('work case')
    benefits_counts = second_labor_answer_per_sentences.count('benefits case')
    union_counts = second_labor_answer_per_sentences.count('union case')
    second_labor_total_counts = {
        employment_counts:'employment case',
        work_counts:'work case',
        benefits_counts:'benefits case',
        union_counts:'union case',
        }
    temp_labor = max(second_labor_total_counts)
    
# tax analyzing
    second_tax_answer_per_sentences = [second_tax_answer(x) for x in lemma_str_sentences]
    income_tax_counts = second_tax_answer_per_sentences.count('income tax case')
    indirect_tax_counts = second_tax_answer_per_sentences.count('indirect tax case')
    excise_tax_counts = second_tax_answer_per_sentences.count('excise tax case')
    stamp_tax_counts = second_tax_answer_per_sentences.count('stamp tax case')
    external_tax_counts = second_tax_answer_per_sentences.count('external tax case')
    second_tax_total_counts = {
        income_tax_counts:'income tax case',
        indirect_tax_counts:'indirect tax case',
        excise_tax_counts:'excise tax case',
        stamp_tax_counts:'stamp tax case',
        external_tax_counts:'external tax case',
        }
    temp_tax = max(second_tax_total_counts)

# total calculation
    gathered_total_counts={
        temp_civil:'civil case',
        temp_commercial:'commercial case',
        temp_criminal:'criminal case',
        temp_labor:'labor case',
        temp_tax:'tax case'
        }
    result = gathered_total_counts.get(max(gathered_total_counts))
    if max(gathered_total_counts)==0:
        st.write('no case detect')
    else:
        st.write('primary category: ',result)
        if result=='civil case':
            st.write('secondary category: ',second_civil_total_counts.get(max(second_civil_total_counts)))
        elif result=='commercial case':
            st.write('secondary category: ',second_commercial_total_counts.get(max(second_commercial_total_counts)))
        elif result=='criminal case':
            st.write('secondary category: ',second_criminal_total_counts.get(max(second_criminal_total_counts)))
        elif result=='labor case':
            st.write('secondary category: ',second_labor_total_counts.get(max(second_labor_total_counts)))
        elif result=='tax case':
            st.write('secondary category: ',second_tax_total_counts.get(max(second_tax_total_counts)))
    
# elif my_page == 'Contributors':
    
#     col1, col2 = st.beta_columns([0.5, 4])

#     col2.write('<span style="font-size:30px; color:#0c45a6"><b>The Team</b></span><br>',
#                unsafe_allow_html=True)
#     st.write('---------------------')

#     col1, col2, col3 = st.beta_columns(3)

#     with col1:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
#         async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
#         data-type="HORIZONTAL" data-vanity="cabenignos" data-version="v1">
#         <a class="badge-base__link LI-simple-link" 
#         href="https://ph.linkedin.com/in/cabenignos?trk=profile-badge"></a></div>''', height=350)

#     with col2:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
#         async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
#         data-type="HORIZONTAL" data-vanity="christopher-louie-jay-gemida-02b083144" data-version="v1">
#         <a class="badge-base__link LI-simple-link" 
#         href="https://ph.linkedin.com/in/christopher-louie-jay-gemida-02b083144?trk=profile-badge"></a></div>''',
#                               height=350)

#     with col3:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
#         async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
#         data-type="HORIZONTAL" data-vanity="fidel-ivan-racines-187477167" data-version="v1">
#         <a class="badge-base__link LI-simple-link" 
#         href="https://ph.linkedin.com/in/fidel-ivan-racines-187477167?trk=profile-badge"></a></div>'''
#                               , height=350)

#     with col1:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="ajloconer" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/ajloconer?trk=profile-badge%22%3EAndrew Justin Oconer</a></div>''',height=350)

#     with col2:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js"
#         async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light"
#         data-type="HORIZONTAL" data-vanity="matthew-antoine-tomas-32011773" data-version="v1">
#         <a class="badge-base__link LI-simple-link"
#         href="https://ph.linkedin.com/in/matthew-antoine-tomas-32011773?trk=profile-badge"></a></div>''',height=350)
        
#     with col3:
#         st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
#         async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
#         data-type="HORIZONTAL" data-vanity="renzo-luis-rodelas-54541b18b" data-version="v1">
#         <a class="badge-base__link LI-simple-link" 
#         href="https://ph.linkedin.com/in/renzo-luis-rodelas-54541b18b?trk=profile-badge"></a></div>''', height=350)
        
#     st.header('The Organization')
#     st.markdown('Eskwelabs is an online data upskilling school for people and teams in Southeast Asia. Who gives '
#                 'access opportunities in the future of work through accessible data skills that are high in-demand as '
#                 'the amount of data in the world increases exponentially.', unsafe_allow_html=False)
    
#     st.markdown('Our mission is to give access to engaging and future-relevant skills education is then crucial to help'
#                 ' people and teams thrive in that future. In Southeast Asia, where more than half of the population is '
#                 'under the age of 30, we believe data education can democratize access to meaningful careers for '
#                 'workers and sustainable competitiveness for companies.', unsafe_allow_html=False)
    
#     st.markdown('At the same time, learning happens in all kinds of ways. Many learning environments, both in school '
#                 'and online, rely on lecture formats which are rarely engaging and effective for technical skills. '
#                 'Eskwelabs aims to enable participatory and active learning experiences so beyond acquiring in-demand '
#                 'skills, we can also rediscover the joy of learning and reinventing ourselves.',
#                 unsafe_allow_html=False)
