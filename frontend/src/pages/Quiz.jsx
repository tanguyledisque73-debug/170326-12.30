import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { 
    ArrowLeft, 
    ArrowRight, 
    CheckCircle2,
    XCircle,
    Clock,
    AlertCircle
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Progress } from '../components/ui/progress';
import Layout from '../components/Layout';
import { getQuizByChapter, getChapter, submitQuiz, getUser } from '../lib/api';
import { toast } from 'sonner';

const Quiz = () => {
    const { chapterId } = useParams();
    const navigate = useNavigate();
    const user = getUser();
    
    const [quiz, setQuiz] = useState(null);
    const [chapter, setChapter] = useState(null);
    const [loading, setLoading] = useState(true);
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [answers, setAnswers] = useState([]);
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [showResult, setShowResult] = useState(false);
    const [result, setResult] = useState(null);
    const [submitting, setSubmitting] = useState(false);

    useEffect(() => {
        if (!user) {
            navigate('/login');
            return;
        }
        loadData();
    }, [chapterId]);

    const loadData = async () => {
        try {
            const [quizData, chapterData] = await Promise.all([
                getQuizByChapter(chapterId),
                getChapter(chapterId)
            ]);
            setQuiz(quizData);
            setChapter(chapterData);
            setAnswers(new Array(quizData.questions.length).fill(-1));
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement du quiz');
        } finally {
            setLoading(false);
        }
    };

    const handleSelectAnswer = (answerIndex) => {
        setSelectedAnswer(answerIndex);
        const newAnswers = [...answers];
        newAnswers[currentQuestion] = answerIndex;
        setAnswers(newAnswers);
    };

    const handleNext = () => {
        if (currentQuestion < quiz.questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
            setSelectedAnswer(answers[currentQuestion + 1] === -1 ? null : answers[currentQuestion + 1]);
        }
    };

    const handlePrevious = () => {
        if (currentQuestion > 0) {
            setCurrentQuestion(currentQuestion - 1);
            setSelectedAnswer(answers[currentQuestion - 1] === -1 ? null : answers[currentQuestion - 1]);
        }
    };

    const handleSubmit = async () => {
        const unanswered = answers.filter(a => a === -1).length;
        if (unanswered > 0) {
            toast.error(`Vous n'avez pas répondu à ${unanswered} question(s)`);
            return;
        }

        setSubmitting(true);
        try {
            const resultData = await submitQuiz({
                quiz_id: quiz.id,
                answers: answers
            });
            setResult(resultData);
            setShowResult(true);
            toast.success('Quiz terminé !');
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la soumission du quiz');
        } finally {
            setSubmitting(false);
        }
    };

    if (loading) {
        return (
            <Layout>
                <div className="flex items-center justify-center min-h-[60vh]">
                    <div className="spinner"></div>
                </div>
            </Layout>
        );
    }

    if (!quiz) {
        return (
            <Layout>
                <div className="max-w-3xl mx-auto px-4 py-8 text-center">
                    <AlertCircle className="w-12 h-12 mx-auto text-slate-400 mb-4" />
                    <p className="text-slate-600 mb-4">Quiz non disponible pour ce chapitre</p>
                    <Link to={`/chapitre/${chapterId}`}>
                        <Button variant="outline">Retour au chapitre</Button>
                    </Link>
                </div>
            </Layout>
        );
    }

    if (showResult && result) {
        return (
            <Layout>
                <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="quiz-result">
                    <Card className="animate-fade-in">
                        <CardHeader className="text-center border-b border-slate-100">
                            <div className={`w-20 h-20 mx-auto rounded-full flex items-center justify-center mb-4 ${
                                result.percentage >= 80 ? 'bg-green-100' : result.percentage >= 60 ? 'bg-yellow-100' : 'bg-red-100'
                            }`}>
                                {result.percentage >= 80 ? (
                                    <CheckCircle2 className="w-10 h-10 text-green-600" />
                                ) : result.percentage >= 60 ? (
                                    <AlertCircle className="w-10 h-10 text-yellow-600" />
                                ) : (
                                    <XCircle className="w-10 h-10 text-red-600" />
                                )}
                            </div>
                            <CardTitle className="text-2xl">
                                {result.percentage >= 80 ? 'Excellent !' : result.percentage >= 60 ? 'Bien !' : 'À revoir'}
                            </CardTitle>
                            <p className="text-slate-600 mt-2">
                                {chapter?.titre}
                            </p>
                        </CardHeader>
                        <CardContent className="p-6">
                            {/* Score */}
                            <div className="text-center mb-8">
                                <div className="text-5xl font-bold mb-2" style={{
                                    color: result.percentage >= 80 ? '#16a34a' : result.percentage >= 60 ? '#d97706' : '#dc2626'
                                }}>
                                    {result.percentage}%
                                </div>
                                <p className="text-slate-600">
                                    {result.score} bonnes réponses sur {result.total}
                                </p>
                            </div>

                            {/* Answers Review */}
                            <div className="space-y-4 mb-8">
                                <h3 className="font-semibold text-slate-900">Détail des réponses</h3>
                                {quiz.questions.map((question, index) => {
                                    const answerDetail = result.answers[index];
                                    return (
                                        <div 
                                            key={question.id}
                                            className={`p-4 rounded-lg border ${
                                                answerDetail?.is_correct 
                                                    ? 'border-green-200 bg-green-50' 
                                                    : 'border-red-200 bg-red-50'
                                            }`}
                                        >
                                            <div className="flex items-start gap-3">
                                                {answerDetail?.is_correct ? (
                                                    <CheckCircle2 className="w-5 h-5 text-green-600 mt-0.5 flex-shrink-0" />
                                                ) : (
                                                    <XCircle className="w-5 h-5 text-red-600 mt-0.5 flex-shrink-0" />
                                                )}
                                                <div className="flex-1">
                                                    <p className="font-medium text-slate-900 text-sm mb-2">
                                                        {question.question}
                                                    </p>
                                                    {!answerDetail?.is_correct && (
                                                        <p className="text-sm text-slate-600">
                                                            <span className="text-red-600">Votre réponse :</span> {question.options[answerDetail?.user_answer]}
                                                            <br />
                                                            <span className="text-green-600">Bonne réponse :</span> {question.options[question.correct_answer]}
                                                        </p>
                                                    )}
                                                    <p className="text-xs text-slate-500 mt-2 italic">
                                                        {question.explication}
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>

                            {/* Actions */}
                            <div className="flex flex-col sm:flex-row gap-3">
                                <Link to={`/chapitre/${chapterId}`} className="flex-1">
                                    <Button variant="outline" className="w-full">
                                        <ArrowLeft className="w-4 h-4 mr-2" />
                                        Revoir le chapitre
                                    </Button>
                                </Link>
                                <Button 
                                    onClick={() => {
                                        setShowResult(false);
                                        setCurrentQuestion(0);
                                        setAnswers(new Array(quiz.questions.length).fill(-1));
                                        setSelectedAnswer(null);
                                    }}
                                    variant="outline"
                                    className="flex-1"
                                    data-testid="retry-quiz-btn"
                                >
                                    Refaire le quiz
                                </Button>
                                <Link to="/dashboard" className="flex-1">
                                    <Button className="w-full bg-red-600 hover:bg-red-700">
                                        Tableau de bord
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            </div>
                        </CardContent>
                    </Card>
                </div>
            </Layout>
        );
    }

    const question = quiz.questions[currentQuestion];
    const progressValue = ((currentQuestion + 1) / quiz.questions.length) * 100;

    return (
        <Layout>
            <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="quiz-page">
                {/* Header */}
                <div className="mb-6">
                    <Link 
                        to={`/chapitre/${chapterId}`}
                        className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-4"
                    >
                        <ArrowLeft className="w-4 h-4" />
                        Retour au chapitre
                    </Link>
                    <h1 className="text-2xl font-bold text-slate-900">
                        {quiz.titre}
                    </h1>
                    <p className="text-slate-600 text-sm mt-1">
                        {chapter?.titre}
                    </p>
                </div>

                {/* Progress */}
                <div className="mb-8">
                    <div className="flex items-center justify-between text-sm text-slate-600 mb-2">
                        <span>Question {currentQuestion + 1} sur {quiz.questions.length}</span>
                        <span>{Math.round(progressValue)}%</span>
                    </div>
                    <Progress value={progressValue} className="h-2" />
                </div>

                {/* Question Card */}
                <Card className="mb-6 animate-fade-in" key={currentQuestion} data-testid="question-card">
                    <CardHeader>
                        <div className="flex items-center gap-2 mb-2">
                            <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                                question.type === 'vrai_faux' 
                                    ? 'bg-blue-100 text-blue-700' 
                                    : 'bg-purple-100 text-purple-700'
                            }`}>
                                {question.type === 'vrai_faux' ? 'Vrai/Faux' : 'QCM'}
                            </span>
                        </div>
                        <CardTitle className="text-lg leading-relaxed">
                            {question.question}
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-3">
                            {question.options.map((option, index) => (
                                <button
                                    key={index}
                                    onClick={() => handleSelectAnswer(index)}
                                    className={`w-full text-left p-4 rounded-lg border-2 transition-all ${
                                        selectedAnswer === index
                                            ? 'border-red-600 bg-red-50'
                                            : 'border-slate-200 hover:border-slate-300 hover:bg-slate-50'
                                    }`}
                                    data-testid={`option-${index}`}
                                >
                                    <div className="flex items-center gap-3">
                                        <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center flex-shrink-0 ${
                                            selectedAnswer === index
                                                ? 'border-red-600 bg-red-600'
                                                : 'border-slate-300'
                                        }`}>
                                            {selectedAnswer === index && (
                                                <div className="w-2 h-2 rounded-full bg-white"></div>
                                            )}
                                        </div>
                                        <span className={`${selectedAnswer === index ? 'text-slate-900 font-medium' : 'text-slate-700'}`}>
                                            {option}
                                        </span>
                                    </div>
                                </button>
                            ))}
                        </div>
                    </CardContent>
                </Card>

                {/* Navigation */}
                <div className="flex items-center justify-between">
                    <Button
                        variant="outline"
                        onClick={handlePrevious}
                        disabled={currentQuestion === 0}
                        data-testid="prev-question-btn"
                    >
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Précédent
                    </Button>

                    {/* Question dots */}
                    <div className="hidden sm:flex items-center gap-1">
                        {quiz.questions.map((_, index) => (
                            <button
                                key={index}
                                onClick={() => {
                                    setCurrentQuestion(index);
                                    setSelectedAnswer(answers[index] === -1 ? null : answers[index]);
                                }}
                                className={`w-3 h-3 rounded-full transition-colors ${
                                    index === currentQuestion
                                        ? 'bg-red-600'
                                        : answers[index] !== -1
                                            ? 'bg-green-500'
                                            : 'bg-slate-300'
                                }`}
                                data-testid={`question-dot-${index}`}
                            />
                        ))}
                    </div>

                    {currentQuestion === quiz.questions.length - 1 ? (
                        <Button
                            onClick={handleSubmit}
                            disabled={submitting}
                            className="bg-red-600 hover:bg-red-700"
                            data-testid="submit-quiz-btn"
                        >
                            {submitting ? (
                                <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                            ) : (
                                <>
                                    Terminer
                                    <CheckCircle2 className="w-4 h-4 ml-2" />
                                </>
                            )}
                        </Button>
                    ) : (
                        <Button
                            onClick={handleNext}
                            disabled={selectedAnswer === null}
                            data-testid="next-question-btn"
                        >
                            Suivant
                            <ArrowRight className="w-4 h-4 ml-2" />
                        </Button>
                    )}
                </div>
            </div>
        </Layout>
    );
};

export default Quiz;
