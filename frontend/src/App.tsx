import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { useAuth } from '@/hooks/useAuth'
import ProtectedRoute from '@/components/ProtectedRoute'
import AuthPage from '@/pages/AuthPage'
import { supabase } from '@/lib/supabase'
import { Button } from '@/components/ui/button'

function ChatPlaceholder() {
  const { user } = useAuth()
  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-4">
      <p className="text-sm text-muted-foreground">Signed in as {user?.email}</p>
      <Button
        variant="outline"
        onClick={() => supabase.auth.signOut()}
      >
        Sign Out
      </Button>
    </div>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<AuthPage />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<ChatPlaceholder />} />
          <Route path="/chat/:threadId?" element={<ChatPlaceholder />} />
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}
