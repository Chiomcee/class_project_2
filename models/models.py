
from sqlalchemy import Integer, String, Date, Boolean, ForeignKey, DateTime, Text, Float, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    
    def __tablename__(cls):
        return cls.__name__.lower()

class Base(DeclarativeBase):
    pass

class ClientProfile(BaseModel, Base):
    __tablename__ = "client_profile"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(100), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(100), insert_default="system")
    unique_id: Mapped[str] = mapped_column(String(64), unique=True)
    first_name: Mapped[str] = mapped_column(String(100))
    middle_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[datetime] = mapped_column(DateTime)
    country_of_birth: Mapped[str] = mapped_column(String(150))
    gender: Mapped[str] = mapped_column(String(30))
    gender_identity: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[Optional[str]] = mapped_column(String(30))
    address: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    state: Mapped[Optional[str]] = mapped_column(String(100))
    zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    country: Mapped[Optional[str]] = mapped_column(String(150))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    ethnicity: Mapped[str] = mapped_column(String(100))
    race: Mapped[str] = mapped_column(String(50))
    sexual_orientation: Mapped[str] = mapped_column(String(64))
    employment_status: Mapped[str] = mapped_column(String(64))
    
class ClientScreening(BaseModel, Base):
    __tablename__ = "client_screening"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_screening: Mapped[datetime] = mapped_column(DateTime)
    health_care_provider: Mapped[str] = mapped_column(String(64))
    reporter_name: Mapped[str] = mapped_column(String(64))
    reporter_contact: Mapped[str] = mapped_column(String(64))
    sexual_partner_gender: Mapped[str] = mapped_column(String(64))
    sexual_partner_gender_identity: Mapped[str] = mapped_column(String(64))
    previous_HIV_screening: Mapped[str] = mapped_column(String(10))
    previous_HIV_screening_date: Mapped[datetime] = mapped_column(DateTime)
    previous_HIV_screening_result: Mapped[str] = mapped_column(String(64))
    reason_for_testing: Mapped[str] = mapped_column(String(64))
    screening_type: Mapped[str] = mapped_column(String(64))
    site_of_sample_collection: Mapped[str] = mapped_column(String(64))
    sample_collection_date: Mapped[datetime] = mapped_column(DateTime)
    screening_result: Mapped[str] = mapped_column(String(64))
    screening_notes: Mapped[Optional[str]] = mapped_column(String(64))
    diagnosis: Mapped[str] = mapped_column(String(64))
    
class ClientTreatment(BaseModel, Base):
    __tablename__ = "client_treatment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_treatment: Mapped[datetime] = mapped_column(DateTime)
    health_care_provider: Mapped[str] = mapped_column(String(64))
    reporter_name: Mapped[str] = mapped_column(String(64))
    reporter_contact: Mapped[str] = mapped_column(String(64))
    treatment_type: Mapped[str] = mapped_column(String(64))
    treatment_plan: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_notes: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_result: Mapped[str] = mapped_column(String(64))
    
class PartnerManagement(BaseModel, Base):
    __tablename__ = "partner_management"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(64), insert_default="system")
    unique_id: Mapped[str] = mapped_column(String(64),unique=True)
    partner_unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_partner_management: Mapped[datetime] = mapped_column(DateTime)
    health_care_provider: Mapped[str] = mapped_column(String(64))
    reporter_name: Mapped[str] = mapped_column(String(64))
    reporter_contact: Mapped[str] = mapped_column(String(64))
    partner_management_type: Mapped[str] = mapped_column(String(64))
    partner_management_plan: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_notes: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_result: Mapped[str] = mapped_column(String(64))
    
    # Model for Congenital Syphilis Case Reporting  
class CongenitalSyphilisReporting(BaseModel, Base):
    __tablename__ = "congenital_syphilis_reporting"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(100), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(100), insert_default="system")
    
    # Reporting Information
    report_date: Mapped[datetime] = mapped_column(DateTime)
    reporting_state: Mapped[str] = mapped_column(String(100))
    reporting_county: Mapped[str] = mapped_column(String(100))
    
    # Maternal Information
    mother_unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    mother_name: Mapped[str] = mapped_column(String(150))
    mother_date_of_birth: Mapped[datetime] = mapped_column(Date)
    mother_state: Mapped[str] = mapped_column(String(100))
    mother_country: Mapped[str] = mapped_column(String(100))
    mother_zip_code: Mapped[str] = mapped_column(String(10))
    mother_dob: Mapped[datetime] = mapped_column(DateTime)
    maternal_obstetric_history: Mapped[str] = mapped_column(String(50))
    maternal_lmp: Mapped[datetime] = mapped_column(DateTime)
    first_prenatal_visit_date: Mapped[datetime] = mapped_column(DateTime)
    first_prenatal_trimester: Mapped[int] = mapped_column(Integer)
    maternal_ethnicity: Mapped[str] = mapped_column(String(50))
    maternal_race: Mapped[str] = mapped_column(Text) 
    marital_status: Mapped[str] = mapped_column(String(30))
    hiv_status: Mapped[str] = mapped_column(String(30)) 
    
    # Infant/Child Information
    delivery_date: Mapped[datetime] = mapped_column(DateTime)
    vital_status: Mapped[str] = mapped_column(String(50))  # Alive/Stillborn
    infant_birth_weight: Mapped[Float] = mapped_column(Float, nullable=True)
    infant_gestational_age: Mapped[int] = mapped_column(Integer)
    infant_non_treponemal_test_result: Mapped[str] = mapped_column(String(50))
    infant_titer: Mapped[str] = mapped_column(String(20))
    infant_treponemal_test_result: Mapped[str] = mapped_column(String(50))
    infant_csf_vdrl_result: Mapped[str] = mapped_column(String(50))
    infant_csf_wbc_protein: Mapped[str] = mapped_column(String(50))
    infant_physical_signs: Mapped[Text] = mapped_column(Text)  
    
    # Test & Treatment Information
    maternal_treatment_date: Mapped[datetime] = mapped_column(DateTime)
    maternal_treatment: Mapped[str] = mapped_column(String(100))  # Treatment type
    maternal_treatment_response: Mapped[str] = mapped_column(String(100), nullable=True)
    maternal_titer: Mapped[str] = mapped_column(String(20), nullable=True)
    infant_treatment: Mapped[Optional[str]] = mapped_column(String(100)) 
    case_classification: Mapped[str] = mapped_column(String(30)) 
    
    # Hepatitis B Infected Pregnant Woman Reporting model
class HepBReportingForm(BaseModel, Base):
    __tablename__ = "hep_b_reporting_form"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(100), insert_default="system")
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_by: Mapped[str] = mapped_column(String(100), insert_default="system")

    
    # Patient Information
    patient_unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE")) #foreign key relationship to ClientProfile
    patient_first_name: Mapped[str] = mapped_column(String(100))
    patient_middle_name: Mapped[Optional[str]] = mapped_column(String(100))
    patient_last_name: Mapped[str] = mapped_column(String(100))
    patient_date_of_birth: Mapped[datetime] = mapped_column(Date)
    patient_gender: Mapped[str] = mapped_column(String(30))
    patient_race: Mapped[str] = mapped_column(String(50))
    patient_ethnicity: Mapped[str] = mapped_column(String(50))
    patient_country_of_birth: Mapped[str] = mapped_column(String(100))
    patient_primary_language: Mapped[Optional[str]] = mapped_column(String(100))
    patient_address: Mapped[str] = mapped_column(String(255))
    patient_city: Mapped[str] = mapped_column(String(100))
    patient_state: Mapped[str] = mapped_column(String(100))
    patient_zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    patient_phone_number: Mapped[Optional[str]] = mapped_column(String(30))
    patient_email: Mapped[Optional[str]] = mapped_column(String(150))
    
    # Clinical Information
    expected_delivery_facility: Mapped[str] = mapped_column(String(255))
    contact_person_at_reporting_facility: Mapped[str] = mapped_column(String(255))
    contact_phone: Mapped[str] = mapped_column(String(20))
    patient_aware_of_status: Mapped[bool] = mapped_column(Boolean)
    estimated_delivery_date: Mapped[datetime] = mapped_column(DateTime)
    ob_provider_last_name: Mapped[str] = mapped_column(String(100))
    ob_provider_first_name: Mapped[str] = mapped_column(String(100))
    
    # Laboratory Information
    reporting_health_care_facility: Mapped[str] = mapped_column(String(255))
    lab_address: Mapped[str] = mapped_column(String(255))
    positive_hbsag: Mapped[bool] = mapped_column(Boolean)
    positive_igm_anti_hbc: Mapped[bool] = mapped_column(Boolean)
    positive_hbeag: Mapped[bool] = mapped_column(Boolean)
    positive_hbv_dna: Mapped[bool] = mapped_column(Boolean)

    # Demographics
    race: Mapped[str] = mapped_column(String(50))  # Example: 'Asian', 'White', etc.
    ethnicity: Mapped[str] = mapped_column(String(50))  # Example: 'Hispanic', 'Non-Hispanic'
    primary_language: Mapped[str] = mapped_column(String(100))
    interpreter_needed: Mapped[bool] = mapped_column(Boolean)
    type_of_insurance: Mapped[str] = mapped_column(String(50))  # Example: 'Private', 'Medicaid', etc.
    notes: Mapped[Text] = mapped_column(Text)  # General remarks or notes.