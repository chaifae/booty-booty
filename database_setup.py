from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    email = Column(String(250), nullable = False)
    image = Column(String(250))


class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    description = Column(String(250))
    image = Column(String(250))


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(250), nullable = False)
    user = relationship(User)


class WorkoutExercise(Base):
    __tablename__ = 'workout-exercise'

    id = Column(Integer, primary_key = True)
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    workout_id = Column(Integer, ForeignKey('workout.id'))
    reps = Column(Integer)
    sets = Column(Integer)
    weight = Column(Integer)
    time = Column(Integer)
    exercise = relationship(Exercise)
    workout = relationship(Workout)


class CompletedExercise(Base):
    __tablename__ = 'completed-workout-exercise'

    id = Column(Integer, primary_key = True)
    workout_exercise_id = Column(Integer, ForeignKey('workout_exercise.id'))
    reps = Column(Integer)
    sets = Column(Integer)
    weight = Column(Integer)
    time = Column(Integer)
    #date = add date-time ref here?
    workout_exercise =relationship(WorkoutExercise)


engine = create_engine('sqlite:///workoutdatabase.db')
Base.metadata.create_all(engine)